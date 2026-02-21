# ⭐ Shunyaya Structural Irreversibility Layer (SSIL)

## Quickstart

**Deterministic • Replay-Verifiable • Conservative Governance**  
**No Equation Modification • No Prediction • No Probabilistic Layer**

---

# What You Need to Know First

Shunyaya Structural Irreversibility Layer (SSIL) is intentionally conservative.

SSIL does not:

- Modify classical magnitude equations  
- Modify thermodynamics or domain physics  
- Predict collapse or failure  
- Inject control logic  
- Perform optimization  
- Apply smoothing or machine learning  
- Use probabilistic inference  

SSIL overlays a **deterministic irreversibility governance layer** over evolving systems.

It:

- Classifies irreversibility posture deterministically  
- Evaluates bounded structural recovery  
- Detects irreversible boundary crossing  
- Governs continuation admissibility  
- Preserves magnitude exactly  
- Produces replay-verifiable artifacts  

---

# Core Invariant (Non-Negotiable)

Conservative collapse mapping:

`phi((m,a,s,r)) = m`

Where:

- `m` = classical magnitude (unchanged)  
- `a` = structural alignment  
- `s` = accumulated posture  
- `r ∈ {R0, E0, I1, I2, C}` = irreversibility regime  

Magnitude is never altered.

---

# Requirements

- Python 3.9+ (CPython recommended)  
- Standard library only  
- No external dependencies  
- Offline-capable execution  

All verification is:

- Deterministic  
- Replay-verifiable  
- Byte-identical across machines  
- Environment-normalized  

No randomness.  
No statistical inference.  
No adaptive thresholds.

---

# What Quickstart Guarantees

If you follow this Quickstart exactly, you will verify:

`B_A = B_B`

without:

- Editing scripts  
- Trusting documentation claims  
- Inspecting internal logic  

Verification proves:

- Deterministic irreversibility classification `{R0, E0, I1, I2, C}`  
- Deterministic bounded horizon `H`  
- Deterministic recovery predicate  
- Deterministic EdgeZero predicate  
- Deterministic continuation mapping `IRR_ADM(t)`  
- Byte-identical artifact generation  
- Conformance manifest replay identity  

If verification fails, SSIL fails.  
There is no partial success.

---

# ⭐ Public Repository Layout

```
SSIL/
├── README.md
├── LICENSE
│
├── docs/
│   ├── Quickstart.md
│   ├── FAQ.md
│   ├── SSIL-Conformance-Specification.md
│   ├── SSIL-Structural-Irreversibility-Model.md
│   ├── SSIL-Structural-Irreversibility-Topology-Diagram.png
│   ├── Concept-Flyer_SSIL_v2.1.pdf
│   └── SSIL_v2.1.pdf
│
├── scripts/
│   └── ssil_engine_v1_2.py
│
├── traces/
│   ├── trace.csv
│   ├── trace_recover.csv
│   ├── trace_e0_then_recover.csv
│   ├── trace_adversarial_A5_starvation.csv
│   └── trace_adversarial_A1_skate.csv
│
├── outputs/
│   └── README.md
│
├── reference_outputs/
│   ├── README.md
│   └── conformance/
│       ├── conformance_manifest.txt
│       ├── conformance_manifest.txt.sha256
│       ├── ssil_case...run1.csv
│       ├── ssil_case...run1.csv.sha256
│       ├── ssil_case...run2.csv
│       ├── ssil_case...run2.csv.sha256
│
└── VERIFY_SSIL_CAPSULE/
    ├── EXPECTED_SHA256.txt
    ├── RUN_VERIFY.bat
    ├── RUN_VERIFY.sh
    └── ssil_capsule_verify.py
```

**Note:**

- `outputs/` remains empty in the repository.  
- `VERIFY_SSIL_CAPSULE/OUT/` is runtime-generated and excluded from version control.

---

# ⭐ Recommended Verification (Capsule Method — Official)

This is the authoritative verification path.

From project root:

### Windows

`VERIFY_SSIL_CAPSULE\RUN_VERIFY.bat`

OR

`python VERIFY_SSIL_CAPSULE\ssil_capsule_verify.py --repo_root . --case recover`

### macOS / Linux

`python VERIFY_SSIL_CAPSULE/ssil_capsule_verify.py --repo_root . --case recover`

Expected result:

`SSIL_CAPSULE_RESULT: PASS`

The capsule verifies:

- Replay identity (`B_A = B_B`)  
- Canonical fingerprint match  
- Locked deterministic profile  
- No formatting drift  
- No parameter mutation  
- No environment deviation  

If fingerprint mismatch occurs:

`SSIL_CAPSULE_RESULT: FAIL`

No tolerance.  
No partial acceptance.  
Byte identity required.

---

# ⭐ Manual Replay Verification (Optional)

Run engine twice:

### Windows

`python scripts\ssil_engine_v1_2.py --in traces\trace_recover.csv --out outputs\run1.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 2.0`

`python scripts\ssil_engine_v1_2.py --in traces\trace_recover.csv --out outputs\run2.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 2.0`

`fc /b outputs\run1.csv outputs\run2.csv`

Replay succeeds only if:

`no differences encountered`

Then verify SHA-256:

`certutil -hashfile outputs\run1.csv SHA256`

Replay identity requires:

`B_A = B_B`

---

# Canonical vs Illustration Parameters

The canonical verification profile locks tighter parameters:

- `delta-max = 0.05`
- `rho = 1.0`

The manual replay example uses:

- `delta-max = 0.15`
- `rho = 2.0`

These values are illustrative and produce different — but still deterministic — outputs.

All conformance fingerprinting and capsule validation use the locked canonical profile.

---

# ⭐ Core Structural Model Overview

Finite irreversibility regime set:

`R = {R0, E0, I1, I2, C}`

Bounded horizon:

`W_H(t) = {t-H+1, ..., t}`

Continuation mapping:

`IRR_ADM(t) ∈ {CONTINUE, ABSTAIN}`

Conservative collapse:

`phi((m,a,s,r)) = m`

SSIL governs continuation — not magnitude.

---

# ⭐ Deterministic Replay Rule

Two independent executions under identical inputs must produce:

`B_A = B_B`

Replay identity is authoritative proof.

---

# ⭐ What SSIL Is Not

SSIL does not:

- Replace thermodynamics  
- Predict cascade failure  
- Forecast market events  
- Simulate mechanical breakdown  
- Inject control signals  
- Guarantee safety  

It governs structural continuation admissibility only.

---

# ⭐ One-Line Summary

Shunyaya Structural Irreversibility Layer (SSIL) introduces a deterministic finite irreversibility grammar `{R0, E0, I1, I2, C}` over evolving systems, preserves classical magnitude via `phi((m,a,s,r)) = m`, governs continuation through `IRR_ADM(t)`, and requires exact replay equivalence `B_A = B_B` as the sole authority of conformance.
