# ⭐ outputs/

This folder is intentionally empty in the public repository.

It serves as the **runtime artifact directory** for SSIL executions.

Artifacts generated here are **ephemeral runtime artifacts** and are **not authoritative conformance evidence**.

---

## Purpose

When executing:

`python scripts\ssil_engine_v1_2.py --in traces\trace_recover.csv --out outputs\run1.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 2.0`

or

`python scripts\ssil_engine_v1_2.py --in traces\trace_recover.csv --out outputs\run2.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 2.0`

Parameters shown above are **illustrative** and may differ from the canonical verification profile.

SSIL will generate deterministic output CSV artifacts inside this folder.

These artifacts demonstrate runtime enforcement of:

- Bounded-horizon window discipline `W_H(t)`
- Deterministic Recovery predicate `Recovery_H(t)`
- Deterministic EdgeZero predicate `EdgeZero_H(t) ∈ {TRUE, FALSE}`
- Structural envelope comparison `A(t) > E_rev(t)`
- Finite irreversibility grammar `{R0, E0, I1, I2, C}`
- Replay identity requirement `B_A = B_B`

---

## What This Folder Is

This folder contains:

- Runtime irreversibility classification CSV outputs
- Replay comparison targets
- Optional hash files (if manually generated)
- Temporary artifacts created during local execution

These files:

- May be deleted safely
- May be regenerated at any time
- Are not sealed
- Are not authoritative

---

## What This Folder Is NOT

This folder is not:

- The canonical conformance evidence bundle
- The replay-verified reference set
- The fingerprint-locked evidence directory
- The authoritative definition of conformance

Authoritative replay-verified artifacts are stored under:

`reference_outputs/`

Cryptographically locked canonical verification is enforced by:

`VERIFY_SSIL_CAPSULE/`

---

## Reproducibility (Manual Replay Demonstration)

To demonstrate deterministic replay identity:

`python scripts\ssil_engine_v1_2.py --in traces\trace_recover.csv --out outputs\run1.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 2.0`

`python scripts\ssil_engine_v1_2.py --in traces\trace_recover.csv --out outputs\run2.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 2.0`

Then compare:

**Windows**

`fc /b outputs\run1.csv outputs\run2.csv`

Expected:

`no differences encountered`

This demonstrates:

`B_A = B_B`

Byte identity is mandatory.

There is:

- No tolerance layer
- No approximate equality
- No probabilistic arbitration

---

## Why This Separation Exists

This strict separation preserves:

- Deterministic execution discipline
- Clear boundary between runtime artifacts and frozen conformance evidence
- Replay-verifiable governance
- EdgeZero transparency
- Irreversibility posture clarity

`outputs/`              → execution  
`reference_outputs/`    → proof  
`VERIFY_SSIL_CAPSULE/`  → institutional verification
