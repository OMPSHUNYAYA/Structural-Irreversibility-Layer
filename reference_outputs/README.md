# ⭐ SSIL Reference Outputs (Frozen Conformance Evidence)

This folder contains **frozen conformance artifacts** produced by executing  
the Shunyaya Structural Irreversibility Layer (SSIL) engine under declared deterministic parameters.

These artifacts demonstrate deterministic irreversibility classification  
under bounded-horizon structural discipline.

They are provided for **audit transparency and inspection only**.

They are not required to execute SSIL,  
and they do not replace independent verification.

---

## What These Reference Outputs Prove

The included bundles demonstrate SSIL’s conformance-critical property:

`B_A = B_B`

Meaning:

- Two independent executions  
- Under identical declared inputs and locked parameters  
- Produce **byte-identical artifacts**

Replay determinism is enforced at the artifact level  
via **SHA-256 sealed output files** and a sealed manifest.

Each conformance case enforces:

- Finite irreversibility regime set `R = {R0, E0, I1, I2, C}`
- Bounded-horizon irreversibility logic  
  `W_H(t) = {t-H+1, ..., t}`
- Deterministic Recovery predicate  
  `Recovery_H(t) ∈ {TRUE, FALSE}`
- Deterministic `EdgeZero_H(t)` predicate  
  `EdgeZero_H(t) ∈ {TRUE, FALSE}`
- Structural envelope comparison  
  `A(t) > E_rev(t)`

This is **deterministic irreversibility classification by replay evidence — not interpretation.**

---

## What These Reference Outputs Contain

Each conformance case includes:

- Irreversibility classification CSV outputs
- SHA-256 hash files for each CSV
- A conformance manifest (`conformance_manifest.txt`)
- A manifest SHA-256 seal (`conformance_manifest.txt.sha256`)

Together, these demonstrate:

- Deterministic asymmetry accumulation
- Deterministic reversibility envelope evolution
- Deterministic Recovery predicate evaluation
- Deterministic `EdgeZero_H(t)` onset detection
- Byte-level artifact sealing

No probabilistic processes are used.  
No adaptive thresholds are permitted.  
No timestamps are embedded.  
No external proprietary datasets are redistributed.

All traces included are deterministic control traces  
or publicly reproducible structural test inputs.

---

## What These Reference Outputs Do NOT Claim

These artifacts do not:

- Perform prediction
- Modify domain equations
- Replace physical law
- Inject control authority
- Guarantee safety
- Provide medical, seismic, financial, or engineering advice
- Certify real-world risk mitigation

SSIL operates strictly at the **structural irreversibility governance layer**.

---

## How to Reproduce (Manual Demonstration)

From project root:

**Windows**

`python scripts\ssil_engine_v1_2.py --in traces\trace_recover.csv --out outputs\run1.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 2.0`

`python scripts\ssil_engine_v1_2.py --in traces\trace_recover.csv --out outputs\run2.csv --H 8 --delta-max 0.15 --s-max 10.0 --rho 2.0`

`fc /b outputs\run1.csv outputs\run2.csv`

Expected:

`no differences encountered`

This reproduces:

`B_A = B_B`

Byte identity is mandatory.  
There is **no tolerance layer**.

---

## Institutional Verification (Authoritative Method)

The authoritative verification path is the verify capsule:

`VERIFY_SSIL_CAPSULE/`

Run:

`python VERIFY_SSIL_CAPSULE\ssil_capsule_verify.py --repo_root . --case recover`

Expected result:

`SSIL_CAPSULE_RESULT: PASS`

The capsule verifies:

- Replay identity
- Canonical parameter lock
- Canonical fingerprint match
- Environment normalization
- Deterministic profile immutability
- Fixed hyperparameter disclosure compliance

The capsule result is binary:

**PASS or FAIL.**

No partial success is possible.

---

## Deterministic Claim Level

SSIL satisfies deterministic discipline at two independent layers:

**Core irreversibility replay identity**

`B_A = B_B`

**Sealed conformance manifest integrity**  
(SHA-256 fingerprint lock)

The frozen reference bundle exists to:

- Provide audit transparency
- Demonstrate deterministic execution
- Allow artifact inspection
- Prove byte-level reproducibility

It does not replace independent replay verification.

SSIL operates as an execution-first deterministic irreversibility governance layer under strict replay discipline.

**Conformance is binary.**
