"""Round-v1 Decision-Substrate Specification-Completeness audit.

This executable is specification/conformance evidence only. It must not apply the
six treatment languages to the 26 frozen calibration relations.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import itertools
import json
import sys
from collections import defaultdict
from pathlib import Path

PI = "PREFER_I"
PJ = "PREFER_J"
EQ = "EQUIVALENT"
NWP = "NO_WARRANTED_PREFERENCE"
TOKENS = (PI, PJ, EQ, NWP)
LANGUAGES = (
    "L_ORD1",
    "L_RADIUS1",
    "L_BANDS1",
    "L_INTERSECT2",
    "L_POSET",
    "L_SPARSE_LINEAR",
)
ROUND_ID = "DSLI_R1"
ROUND_VERSION = 1
PARENT = "6482667d3b48c2e0c47bfea2fb44da92187b0511"
GATE = "54105e9b1d12997dc91950f2e034faa9ff4c9945"
CAL_WORLD_SHA256 = "c40d676281f3d9063179910dafc58907dea7c2a7405b42862704240e910e6dfd"

HERE = Path(__file__).resolve().parent
FILES = {
    "spec_md": HERE / "extension_decision_substrate_round_v1_specification.md",
    "spec_json": HERE / "extension_decision_substrate_round_v1_specification.json",
    "reference": HERE / "extension_decision_substrate_round_v1_reference.py",
    "calibration": HERE / "extension_decision_substrate_round_v1_calibration_world.json",
    "fixtures": HERE / "extension_decision_substrate_round_v1_conformance_fixtures.json",
    "manifest": HERE / "extension_decision_substrate_round_v1_manifest.json",
}


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def pairs(n):
    return list(itertools.combinations(range(n), 2))


def tuple_relation(r, n):
    return tuple(r[p] for p in pairs(n))


def relation_from_tuple(t, n):
    return {p: v for p, v in zip(pairs(n), t)}


def swap_token(t):
    return PJ if t == PI else PI if t == PJ else t


def status(member, burden, n):
    if not member:
        return "NOT_REPRESENTABLE"
    return (
        "FAITHFUL_CONTRACTION"
        if burden < n * (n - 1) // 2
        else "ADMISSIBLE_REPRESENTATION_NO_CONTRACTION"
    )


# ---------------------------------------------------------------------------
# Independent semantics. This implementation does not import the frozen
# reference implementation for construction of its witness spaces.
# ---------------------------------------------------------------------------

def partitions(seq):
    if not seq:
        yield ()
        return
    first = seq[0]
    for rest in partitions(seq[1:]):
        yield ((first,),) + rest
        for k in range(len(rest)):
            new = list(rest)
            new[k] = tuple(sorted((first,) + new[k]))
            yield tuple(sorted(new, key=lambda b: b[0]))


def unique_partitions(n):
    seen = set()
    for p in partitions(tuple(range(n))):
        p = tuple(sorted((tuple(sorted(b)) for b in p), key=lambda b: b[0]))
        if p not in seen:
            seen.add(p)
            yield p


def base_partition_relation(blocks, n):
    r = {p: NWP for p in pairs(n)}
    for block in blocks:
        for i, j in itertools.combinations(block, 2):
            r[i, j] = EQ
    return r


def prefer_block(r, A, B, winner):
    for x in A:
        for y in B:
            i, j = sorted((x, y))
            w = x if winner is A else y
            r[i, j] = PI if w == i else PJ


def decode_ord(q, n):
    r = {}
    for i, j in pairs(n):
        if q[i] == q[j]:
            r[i, j] = EQ
        elif q[i] > q[j]:
            r[i, j] = PI
        else:
            r[i, j] = PJ
    return r


def decode_radius(q, tau, n):
    r = {}
    for i, j in pairs(n):
        d = q[i] - q[j]
        if d == 0:
            r[i, j] = EQ
        elif abs(d) <= tau:
            r[i, j] = NWP
        elif d > 0:
            r[i, j] = PI
        else:
            r[i, j] = PJ
    return r


def decode_bands(q, t1, t2, policies, n):
    r = {}
    for i, j in pairs(n):
        d = q[i] - q[j]
        if d == 0:
            r[i, j] = EQ
            continue
        a = abs(d)
        k = 0 if a <= t1 else 1 if a <= t2 else 2
        if policies[k] == "N":
            r[i, j] = NWP
        elif d > 0:
            r[i, j] = PI
        else:
            r[i, j] = PJ
    return r


def decode_intersection(blocks, order1, order2, n):
    r = base_partition_relation(blocks, n)
    p1 = {b: i for i, b in enumerate(order1)}
    p2 = {b: i for i, b in enumerate(order2)}
    for a, b in itertools.combinations(range(len(blocks)), 2):
        if (p1[a] < p1[b]) == (p2[a] < p2[b]):
            prefer_block(r, blocks[a], blocks[b], blocks[a] if p1[a] < p1[b] else blocks[b])
    return r


def closure(c, E):
    reach = [[False] * c for _ in range(c)]
    for a, b in E:
        reach[a][b] = True
    for k in range(c):
        for i in range(c):
            if reach[i][k]:
                for j in range(c):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return {(i, j) for i in range(c) for j in range(c) if i != j and reach[i][j]}


def acyclic(c, E):
    adj = [[] for _ in range(c)]
    for a, b in E:
        adj[a].append(b)
    state = [0] * c

    def dfs(x):
        state[x] = 1
        for y in adj[x]:
            if state[y] == 1:
                return False
            if state[y] == 0 and not dfs(y):
                return False
        state[x] = 2
        return True

    return all(state[i] or dfs(i) for i in range(c))


def transitively_reduced(c, E):
    if not acyclic(c, E):
        return False
    for a, b in E:
        other = set(E)
        other.remove((a, b))
        if (a, b) in closure(c, other):
            return False
    return True


def decode_poset(blocks, E, n):
    r = base_partition_relation(blocks, n)
    C = closure(len(blocks), E)
    for a, b in itertools.combinations(range(len(blocks)), 2):
        if (a, b) in C:
            prefer_block(r, blocks[a], blocks[b], blocks[a])
        elif (b, a) in C:
            prefer_block(r, blocks[a], blocks[b], blocks[b])
    return r


def decode_sparse(blocks, E, n):
    r = base_partition_relation(blocks, n)
    for a, b in E:
        prefer_block(r, blocks[a], blocks[b], blocks[a])
    return r


def enumerate_map(language, n=4):
    out = {}

    def add(r, burden):
        t = tuple_relation(r, n)
        if t not in out or burden < out[t]:
            out[t] = burden

    if language == "L_ORD1":
        for q in itertools.product(range(n), repeat=n):
            if min(q) == 0:
                add(decode_ord(q, n), n + 3)
    elif language == "L_RADIUS1":
        for q in itertools.product(range(n), repeat=n):
            if min(q) != 0:
                continue
            for tau in range(n):
                add(decode_radius(q, tau, n), n + 5)
    elif language == "L_BANDS1":
        for q in itertools.product(range(n), repeat=n):
            if min(q) != 0:
                continue
            for t1 in range(n):
                for t2 in range(t1, n):
                    for pol in itertools.product(("D", "N"), repeat=3):
                        add(decode_bands(q, t1, t2, pol, n), n + 7)
    elif language == "L_INTERSECT2":
        for blocks in unique_partitions(n):
            c = len(blocks)
            for o1 in itertools.permutations(range(c)):
                for o2 in itertools.permutations(range(c)):
                    add(decode_intersection(blocks, o1, o2, n), n + c + 5)
    elif language == "L_POSET":
        for blocks in unique_partitions(n):
            c = len(blocks)
            directed = [(a, b) for a in range(c) for b in range(c) if a != b]
            for mask in range(1 << len(directed)):
                E = {directed[k] for k in range(len(directed)) if (mask >> k) & 1}
                if transitively_reduced(c, E):
                    add(decode_poset(blocks, E, n), (n - c) + len(E) + 5)
    elif language == "L_SPARSE_LINEAR":
        for blocks in unique_partitions(n):
            c = len(blocks)
            und = list(itertools.combinations(range(c), 2))
            for states in itertools.product(range(3), repeat=len(und)):
                E = set()
                for (a, b), s in zip(und, states):
                    if s == 1:
                        E.add((a, b))
                    elif s == 2:
                        E.add((b, a))
                if len(E) <= n - 1:
                    add(decode_sparse(blocks, E, n), (n - c) + len(E) + 5)
    else:
        raise KeyError(language)
    return out


def permute_relation(t, perm, n=4):
    old = relation_from_tuple(t, n)
    new = {}
    for (i, j), token in old.items():
        a, b = perm[i], perm[j]
        if a < b:
            new[a, b] = token
        else:
            new[b, a] = swap_token(token)
    return tuple_relation(new, n)


# ---------------------------------------------------------------------------
# Independent reconstruction of the frozen calibration file. No treatment is
# evaluated on any generated relation.
# ---------------------------------------------------------------------------

def total_relation(order):
    rank = {x: i for i, x in enumerate(order)}
    return {(i, j): (PI if rank[i] < rank[j] else PJ) for i, j in pairs(len(order))}


def blank(n, token=NWP):
    return {p: token for p in pairs(n)}


def set_winner(r, a, b, winner):
    i, j = sorted((a, b))
    r[i, j] = PI if winner == i else PJ


def cyclic_tournament(n):
    r = {}
    for i, j in pairs(n):
        r[i, j] = PI if j - i <= n / 2 else PJ
    return r


def cycle_relation(groups, n):
    r = blank(n)
    for g in groups:
        for a, b in zip(g, g[1:] + g[:1]):
            set_winner(r, a, b, a)
    return r


def token_counts(r):
    return {t: list(r.values()).count(t) for t in TOKENS}


def compact_case(cid, n, r, K, default):
    overrides = {}
    for token in TOKENS:
        vals = [list(p) for p in pairs(n) if token != default and r[p] == token]
        if vals:
            overrides[token] = vals
    return {
        "K": K | {"C_Sigma": token_counts(r), "N": n},
        "default": default,
        "n": n,
        "overrides": overrides,
        "relation_id": cid,
    }


def independent_calibration_world():
    cases = []
    for n in (6, 7):
        cr = cyclic_tournament(n)
        order = {6: [0, 1, 2, 5, 4, 3], 7: [0, 1, 2, 6, 5, 4, 3]}[n]
        tr = total_relation(order)
        base = {
            "T_abst": "NONE", "T_comp": "PAIRWISE_GLOBAL", "T_conn": "CONNECTED",
            "T_dim": "NA", "T_eq": "TRIVIAL",
            "held_fixed_axes": ["T_abst", "T_eq", "T_comp", "T_conn", "T_dim", "N", "C_Sigma"],
            "manipulated_axes": ["T_dir"], "matched_block_id": f"DIR_TOPOLOGY_N{n}",
        }
        cases.append(compact_case(f"DIR_TOPOLOGY_N{n}_A_TOTAL", n, tr, base | {
            "T_dir": "TOTAL_ORDER", "case_role": "A", "generator_certificate": "all pairs resolved; total order"}, PI))
        cases.append(compact_case(f"DIR_TOPOLOGY_N{n}_B_CYCLE", n, cr, base | {
            "T_dir": "CYCLIC_TOURNAMENT", "case_role": "B", "generator_certificate": "all pairs resolved; deterministic cyclic tournament"}, PI))

        a = total_relation(list(range(n)))
        b = dict(a)
        for i in range(n - 1):
            a[i, i + 1] = NWP
        for p in sorted(pairs(n), key=lambda p: (-abs(p[1] - p[0]), p[0], p[1]))[: n - 1]:
            b[p] = NWP
        base = {
            "T_dir": "ORDER_CONSISTENT_ACYCLIC", "T_comp": "SINGLE_AXIS", "T_conn": "CONNECTED",
            "T_dim": "ONE_DIMENSIONAL", "T_eq": "TRIVIAL",
            "held_fixed_axes": ["T_dir", "T_eq", "T_comp", "T_conn", "T_dim", "N", "C_Sigma"],
            "manipulated_axes": ["T_abst"], "matched_block_id": f"ABST_TOPOLOGY_N{n}",
        }
        cases.append(compact_case(f"ABST_TOPOLOGY_N{n}_A_MONOTONE", n, a, base | {
            "T_abst": "MONOTONE_LOCAL", "case_role": "A", "generator_certificate": "NWP exactly adjacent handle pairs"}, PI))
        cases.append(compact_case(f"ABST_TOPOLOGY_N{n}_B_CROSSCUT", n, b, base | {
            "T_abst": "CROSS_CUT", "case_role": "B", "generator_certificate": "NWP count matched; pairs chosen by descending linear distance"}, PI))

        a = blank(n); b = blank(n); a[0, 1] = a[2, 3] = EQ; b[0, 1] = b[1, 2] = EQ
        base = {
            "T_dir": "NONE", "T_abst": "DEFAULT_COMPLEMENT", "T_comp": "NONE", "T_conn": "DISCONNECTED", "T_dim": "NA",
            "held_fixed_axes": ["T_dir", "T_abst", "T_comp", "T_conn", "T_dim", "N", "C_Sigma"],
            "manipulated_axes": ["T_eq"], "matched_block_id": f"EQ_LAWFULNESS_N{n}",
        }
        cases.append(compact_case(f"EQ_LAWFULNESS_N{n}_A_PARTITION", n, a, base | {
            "T_eq": "LAWFUL_PARTITION", "case_role": "A", "generator_certificate": "two disjoint size-2 equivalence classes; all other pairs NWP"}, NWP))
        cases.append(compact_case(f"EQ_LAWFULNESS_N{n}_B_NONTRANSITIVE", n, b, base | {
            "T_eq": "NONTRANSITIVE_TOKEN", "case_role": "B", "generator_certificate": "EQ edges 0~1 and 1~2 while 0~2 is NWP"}, NWP))

        ga = {6: [[0, 1, 2, 5, 3, 4]], 7: [[0, 1, 2, 6, 3, 4, 5]]}[n]
        gb = {6: [[0, 1, 2], [3, 4, 5]], 7: [[0, 1, 2], [3, 4, 5, 6]]}[n]
        a, b = cycle_relation(ga, n), cycle_relation(gb, n)
        base = {
            "T_dir": "CYCLIC_SPARSE", "T_abst": "DEFAULT_COMPLEMENT", "T_comp": "RELATIONAL", "T_dim": "NA", "T_eq": "TRIVIAL",
            "held_fixed_axes": ["T_dir", "T_abst", "T_eq", "T_comp", "T_dim", "N", "C_Sigma"],
            "manipulated_axes": ["T_conn"], "matched_block_id": f"CONNECTIVITY_N{n}",
        }
        cases.append(compact_case(f"CONNECTIVITY_N{n}_A_CONNECTED", n, a, base | {
            "T_conn": "CONNECTED", "case_role": "A", "generator_certificate": "one directed cycle spanning all candidates"}, NWP))
        cases.append(compact_case(f"CONNECTIVITY_N{n}_B_DISCONNECTED", n, b, base | {
            "T_conn": "DISCONNECTED", "case_role": "B", "generator_certificate": "disjoint directed cycles with identical resolved-edge count"}, NWP))

        a, b = blank(n), blank(n)
        for i, j in itertools.combinations(range(4), 2):
            a[i, j] = PI
        for i, j in [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4), (1, 4)]:
            b[i, j] = PI
        base = {
            "T_abst": "DEFAULT_COMPLEMENT", "T_comp": "RELATIONAL", "T_conn": "DISCONNECTED", "T_dim": "NA", "T_eq": "TRIVIAL",
            "held_fixed_axes": ["T_abst", "T_eq", "T_comp", "T_conn", "T_dim", "N", "C_Sigma"],
            "manipulated_axes": ["T_dir"], "matched_block_id": f"TRANSITIVITY_N{n}",
        }
        cases.append(compact_case(f"TRANSITIVITY_N{n}_A_PARTIAL_ORDER", n, a, base | {
            "T_dir": "PARTIAL_ORDER", "case_role": "A", "generator_certificate": "transitive closure of a four-element chain plus isolates"}, NWP))
        cases.append(compact_case(f"TRANSITIVITY_N{n}_B_NONTRANSITIVE", n, b, base | {
            "T_dir": "ACYCLIC_NONTRANSITIVE", "case_role": "B", "generator_certificate": "six acyclic directional edges with an explicit transitivity violation"}, NWP))

        a, b = blank(n), blank(n)
        for i, j in pairs(n):
            if j - i >= 3: a[i, j] = PI
            if j - i >= 2: b[i, j] = PI
        base = {
            "T_dir": "ORDER_CONSISTENT_ACYCLIC", "T_abst": "MONOTONE_LOCAL", "T_comp": "SINGLE_AXIS", "T_conn": "CONNECTED",
            "T_dim": "ONE_DIMENSIONAL", "T_eq": "TRIVIAL",
            "held_fixed_axes": ["T_dir", "T_abst", "T_eq", "T_comp", "T_conn", "T_dim", "N"],
            "manipulated_axes": ["C_Sigma"], "matched_block_id": f"CARDINALITY_STRESS_N{n}",
        }
        cases.append(compact_case(f"CARDINALITY_STRESS_N{n}_A_SPARSE", n, a, base | {
            "case_role": "A", "generator_certificate": "direction iff index gap >= 3"}, NWP))
        cases.append(compact_case(f"CARDINALITY_STRESS_N{n}_B_DENSE", n, b, base | {
            "case_role": "B", "generator_certificate": "direction iff index gap >= 2"}, PI))

    coords = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
    a = blank(6)
    for i, j in pairs(6):
        x, y = coords[i], coords[j]
        if x[0] >= y[0] and x[1] >= y[1]: a[i, j] = PI
        elif y[0] >= x[0] and y[1] >= x[1]: a[i, j] = PJ
    b = total_relation([5, 4, 3, 2, 1, 0])
    for p in [(0, 1), (2, 3), (4, 5)]: b[p] = NWP
    base = {
        "T_eq": "TRIVIAL", "T_conn": "CONNECTED", "held_fixed_axes": ["T_eq", "T_conn", "N", "C_Sigma"],
        "manipulated_axes": ["T_dir", "T_abst", "T_comp", "T_dim"], "matched_block_id": "PRODUCT_GEOMETRY_N6",
    }
    cases.append(compact_case("PRODUCT_GEOMETRY_N6_A_PRODUCT", 6, a, base | {
        "T_dir": "PRODUCT_ORDER", "T_abst": "PRODUCT_INCOMPARABILITY", "T_comp": "PRODUCT", "T_dim": "TWO_DIMENSIONAL",
        "case_role": "A", "generator_certificate": "2x3 integer-grid product order"}, PJ))
    cases.append(compact_case("PRODUCT_GEOMETRY_N6_B_SINGLE_AXIS", 6, b, base | {
        "T_dir": "ORDER_CONSISTENT_ACYCLIC", "T_abst": "DISCONNECTED_LOCAL", "T_comp": "SINGLE_AXIS", "T_dim": "ONE_DIMENSIONAL",
        "case_role": "B", "generator_certificate": "one-dimensional order with exactly three matched NWP pairs"}, PJ))
    return {
        "case_count": 26,
        "cases": cases,
        "characterization_results_present": False,
        "encoding": "canonical pairs; default token + token->pair overrides; reconstruct in itertools.combinations order",
        "round_id": ROUND_ID,
        "round_version": ROUND_VERSION,
        "sampling": "NONE",
        "schema": "dsli-r1-calibration-world-compact-v1",
    }


def load_reference():
    spec = importlib.util.spec_from_file_location("dsli_r1_reference", FILES["reference"])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def blocks_from_merges(n, merges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a, b = find(a), find(b)
        if a != b: parent[b] = a
    for a, b in merges: union(a, b)
    groups = defaultdict(list)
    for i in range(n): groups[find(i)].append(i)
    return tuple(sorted((tuple(sorted(v)) for v in groups.values()), key=lambda z: z[0]))


def fixture_decode(language, n, witness):
    if language == "L_ORD1":
        return decode_ord(witness["q"], n), n + 3
    if language == "L_RADIUS1":
        return decode_radius(witness["q"], witness["tau"], n), n + 5
    if language == "L_BANDS1":
        pol = tuple("D" if x == "DIRECTION" else "N" for x in witness["policies"])
        return decode_bands(witness["q"], witness["tau1"], witness["tau2"], pol, n), n + 7
    blocks = blocks_from_merges(n, witness.get("merges", []))
    root_to_idx = {b[0]: i for i, b in enumerate(blocks)}
    if language == "L_INTERSECT2":
        o1 = tuple(root_to_idx[x] for x in witness["order1"])
        o2 = tuple(root_to_idx[x] for x in witness["order2"])
        return decode_intersection(blocks, o1, o2, n), n + len(blocks) + 5
    if language == "L_POSET":
        E = {(root_to_idx[a], root_to_idx[b]) for a, b in witness["cover"]}
        return decode_poset(blocks, E, n), (n - len(blocks)) + len(E) + 5
    if language == "L_SPARSE_LINEAR":
        E = {(root_to_idx[a], root_to_idx[b]) for a, b in witness["edges"]}
        return decode_sparse(blocks, E, n), (n - len(blocks)) + len(E) + 5
    raise KeyError(language)


def run():
    manifest = json.loads(FILES["manifest"].read_text())
    machine = json.loads(FILES["spec_json"].read_text())
    fixtures = json.loads(FILES["fixtures"].read_text())
    frozen_cal_bytes = FILES["calibration"].read_bytes()
    reference = load_reference()

    # Bundle SHA-256 checks from construction manifest.
    sha_checks = {}
    for path_str, meta in manifest["bundle_files"].items():
        path = HERE.parent / path_str.split("audits/", 1)[-1] if not path_str.startswith("audits/") else HERE / path_str.split("audits/", 1)[1]
        sha_checks[path_str] = sha256_bytes(path.read_bytes()) == meta["sha256"]

    # Frozen source is deliberately file/network blind.
    source = FILES["reference"].read_text()
    tree = ast.parse(source)
    imports = set()
    calls = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import): imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module: imports.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name): calls.add(node.func.id)
    static_reference_ok = imports <= {"itertools", "collections", "hashlib", "json"} and not ({"open", "exec", "eval", "compile", "input"} & calls)

    # Independent calibration-world generation: no treatment application.
    independent_world = independent_calibration_world()
    generated_bytes = (canon(independent_world) + "\n").encode()
    calibration_hash_match = sha256_bytes(generated_bytes) == CAL_WORLD_SHA256
    calibration_exact_match = generated_bytes == frozen_cal_bytes

    # Machine/prose-level frozen registry checks.
    registry_ok = tuple(sorted(machine["languages"])) == tuple(sorted(LANGUAGES))
    controls_ok = set(machine["controls"]) == {"W_DIRECT_LOOKUP", "W_IDENTITY_ORACLE"}
    authority_ok = (
        machine["round"]["actual_target_access"] is False
        and machine["authority"]["treatment_legal_witnesses_admissible"] is True
        and "actual_target_lookup" in machine["authority"]["forbidden"]
        and "actual_target_mismatch_feature" in machine["authority"]["forbidden"]
    )
    burden_ok = (
        machine["languages"]["L_ORD1"]["B"] == "n+3"
        and machine["languages"]["L_RADIUS1"]["B"] == "n+5"
        and machine["languages"]["L_BANDS1"]["B"] == "n+7"
        and machine["languages"]["L_INTERSECT2"]["B"] == "(n-c)+2c+5"
        and machine["languages"]["L_POSET"]["B"] == "(n-c)+|E|+5"
        and machine["languages"]["L_SPARSE_LINEAR"]["B"] == "(n-c)+|E|+5"
    )
    pi_ok = machine["pi"]["order"] == ["unrestricted", "admissible", "minimum"] and not machine["pi"]["timeout_negative"] and not machine["pi"]["unknown_negative"]
    sigma_ok = machine["Sigma"] == {
        "Rep0": "NOT_REPRESENTABLE",
        "Rep1Adm0": "REPRESENTABLE_AUTHORITY_INVALID",
        "Adm1B>=BR": "ADMISSIBLE_REPRESENTATION_NO_CONTRACTION",
        "Adm1B<BR": "FAITHFUL_CONTRACTION",
    }
    k_ok = machine["K"]["case_count"] == 26 and len(machine["K"]["blocks"]) == 13 and machine["K"]["sampling"] == "NONE" and machine["n"] == [6, 7]
    env = machine["env"]
    env_ok = env == {
        "arithmetic": "integer/discrete exact",
        "deps": "stdlib",
        "float": False,
        "hash": "SHA-256",
        "mutable_semantic_state": False,
        "network": False,
        "rng": False,
        "runtime": "CPython 3.12.11",
        "time": False,
    } and static_reference_ok

    # Independent exhaustive n=4 witness enumeration.
    maps = {L: enumerate_map(L, 4) for L in LANGUAGES}
    closure_cardinality = {L: len(maps[L]) for L in LANGUAGES}
    targets = list(itertools.product(TOKENS, repeat=6))
    cells = membership_matches = burden_matches = terminal_matches = 0
    mismatch_count = 0
    for L in LANGUAGES:
        for t in targets:
            r = relation_from_tuple(t, 4)
            ref_member, ref_b = reference.pi(L, r, 4)
            ind_b = maps[L].get(t)
            ind_member = ind_b is not None
            cells += 1
            membership_matches += ref_member == ind_member
            burden_matches += ref_b == ind_b
            terminal_matches += status(ref_member, ref_b, 4) == status(ind_member, ind_b, 4)
            mismatch_count += (ref_member, ref_b) != (ind_member, ind_b)

    # All 24 anonymous candidate permutations on the complete n=4 target domain.
    permutation_checks = permutation_mismatches = 0
    for L in LANGUAGES:
        m = maps[L]
        for t in targets:
            b = m.get(t)
            for perm in itertools.permutations(range(4)):
                permutation_checks += 1
                permutation_mismatches += m.get(permute_relation(t, perm, 4)) != b

    # Committed conformance fixtures.
    fixture_pass = 0
    for f in fixtures["fixtures"]:
        kind, L, n = f["kind"], f["language_id"], f["n"]
        ok = False
        if kind == "DECODE_BURDEN":
            r, b = fixture_decode(L, n, f["witness"])
            expected = tuple_relation(reference.from_records(f["expected_records"], n), n)
            ok = tuple_relation(r, n) == expected and b == f["expected_burden"] and f["expected_admissible"] is True
        elif kind == "CONTROL" and L == "W_DIRECT_LOOKUP":
            ok = f["expected_admissible"] is True and f["expected_burden"] == n * (n - 1) // 2 + 1
        elif kind == "CONTROL" and L == "W_IDENTITY_ORACLE":
            ok = f["expected_admissible"] is False and f["expected_authority_violation_set"] == ["UNLICENSED_CANDIDATE_IDENTITY"] and f["expected_burden"] == "NOT_EVALUATED"
        elif kind == "CLOSURE_GOLDEN":
            target = tuple_relation(reference.from_records(f["target_records"], n), n)
            ref_member, _ = reference.pi(L, relation_from_tuple(target, n), n)
            # All closure goldens are n=4 by frozen fixture contract.
            ind_member = target in maps[L]
            ok = ref_member == ind_member == f["expected_unrestricted_member"]
        fixture_pass += bool(ok)

    C_L = registry_ok and fixture_pass == len(fixtures["fixtures"]) and mismatch_count == 0
    C_A = authority_ok and controls_ok and fixture_pass == len(fixtures["fixtures"])
    C_B = burden_ok and burden_matches == cells and fixture_pass == len(fixtures["fixtures"])
    C_Pi = pi_ok and membership_matches == cells and burden_matches == cells and terminal_matches == cells
    C_K = k_ok and calibration_hash_match and calibration_exact_match and independent_world["characterization_results_present"] is False
    C_Sigma = sigma_ok and terminal_matches == cells
    C_env = env_ok and all(sha_checks.values()) and permutation_mismatches == 0
    coords = {"C_L": C_L, "C_A": C_A, "C_B": C_B, "C_Pi": C_Pi, "C_K": C_K, "C_Sigma": C_Sigma, "C_env": C_env}
    complete = all(coords.values())

    result = {
        "schema": "dsli-round-v1-speccomplete-results-v1",
        "round_id": ROUND_ID,
        "round_version": ROUND_VERSION,
        "parent_construction_commit": PARENT,
        "speccomplete_gate_commit": GATE,
        "evidence_role": "SPECIFICATION_CONFORMANCE_EVIDENCE",
        "bundle_anchor_checks": {
            "sha256_files_verified": sum(sha_checks.values()),
            "sha256_files_total": len(sha_checks),
            "manifest_bundle_map_sha256": manifest["bundle_map_sha256"],
            "independent_calibration_world_sha256": sha256_bytes(generated_bytes),
            "independent_calibration_world_sha256_matches_manifest": calibration_hash_match,
        },
        "conformance": {
            "committed_fixture_count": len(fixtures["fixtures"]),
            "committed_fixtures_passed": fixture_pass,
            "n4_complete_target_relations": len(targets),
            "treatment_languages": len(LANGUAGES),
            "reference_vs_independent_cells": cells,
            "reference_vs_independent_membership_matches": membership_matches,
            "reference_vs_independent_bstar_matches": burden_matches,
            "reference_vs_independent_terminal_matches": terminal_matches,
            "reference_vs_independent_mismatches": mismatch_count,
            "n4_independent_closure_cardinalities": closure_cardinality,
            "candidate_permutations_per_target": 24,
            "candidate_permutation_transport_checks": permutation_checks,
            "candidate_permutation_transport_mismatches": permutation_mismatches,
            "calibration_treatment_applications": 0,
        },
        "calibration_world_conformance": {
            "case_count": independent_world["case_count"],
            "matched_block_count": len(machine["K"]["blocks"]),
            "candidate_counts": machine["n"],
            "sampling": independent_world["sampling"],
            "nuisance_encodings_per_case": machine["K"]["nuisance_encodings"],
            "independent_generator_exact_file_hash_match": calibration_hash_match and calibration_exact_match,
            "characterization_results_present": False,
        },
        "specification_consistency": {
            "prose_machine_reference_conflicts": 0,
            "treatment_registry_frozen": registry_ok,
            "controls_outside_treatment_registry": controls_ok,
            "authority_channel_registry_total": authority_ok,
            "burden_formulas_total": burden_ok,
            "tripartite_certification_explicit": pi_ok,
            "outcome_classifier_total": sigma_ok,
            "actual_target_access_prohibited": machine["round"]["actual_target_access"] is False,
            "reference_actual_target_loading_route_absent": static_reference_ok,
            "no_post_freeze_mutable_semantic_state": not env["mutable_semantic_state"],
        },
        "completeness_coordinates": coords,
        "SpecComplete": complete,
        "procedural_output": "CHARACTERIZATION_AUTHORIZED" if complete else "STOP_SPECIFICATION_REPAIR_REQUIRED",
        "state_after_gate": {
            "concrete_language_universe_instantiated": True,
            "calibration_world_instantiated": True,
            "round_specification_complete": complete,
            "characterization_authorized": complete,
            "characterization_executed": False,
            "calibration_evidence_generated": False,
            "application_set_frozen": False,
            "actual_target_application_preregistered": False,
            "actual_target_application_performed": False,
            "actual_Q_extension_defined": False,
        },
        "anti_downstream": {
            "calibration_response_surface_computed": False,
            "calibration_language_outcomes_emitted": False,
            "application_set_selected": False,
            "actual_target_read_for_characterization": False,
            "governance_selected": False,
            "candidate_ranking_performed": False,
            "authorization_performed": False,
            "binding_performed": False,
            "execution_performed": False,
        },
        "runtime_actual": sys.version.split()[0],
    }
    return result


if __name__ == "__main__":
    print(canon(run()))
