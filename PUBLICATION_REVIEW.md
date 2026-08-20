# Publication Review — nora-capabilities

**Status: BLOCKED**

This review is fail-closed. A scaffold cannot pass it merely because required files exist.

## Closeout status

- Technical publication preparation complete.
- G5 rights/provenance review executed 2026-08-20 — **result: BLOCKED** (see `RIGHTS_REVIEW.md`).
- Repository remains private.
- No visibility authorization has been granted.

## Evidence (2026-08-20)

- **G0 identity**: clean target history from "Initial clean scaffold baseline" (0c0a11b); no legacy repo reused.
- **G1 technical**: `make doctor` PASS, `make validate` PASS, pytest 6 passed; `examples/demo.py` exit 0 (governance/redaction PASS). HEAD `c9659d9`.
- **G2 claims**: CURRENT_STATE.md test count 6 matches; no production-ready claims.
- **G3 privacy / G4 secrets**: working-tree + full-history scans PASS (2026-08-20, `/tmp/scan2_*.log`); only synthetic redaction fixture values (`[REDACTED]`) matched by design.
- **G5 rights/provenance**: review executed 2026-08-20 — **BLOCKED** (PROV-CAP-001 agent-platform: **RIGHTS UNCLEAR** — no LICENSE file; PROV-CAP-002 agent-control-plane: **SOURCE UNKNOWN** — recorded commit `69e120aa` does not exist on GitHub, no LICENSE file; Canon: no Canon material found in history). See `RIGHTS_REVIEW.md`.
- **G6 contributor readiness**: CONTRIBUTING/CODE_OF_CONDUCT/SECURITY/ROADMAP/ARCHITECTURE present; issue + PR templates; 6 issue seeds; good-first-issue #4 open.
- **G7 pre-flip remote assurance**: ci PASS on pushed main (runs 32335416502, 32334864753); codeql workflow pinned v4 + actions:read (commit e25bacc).
- **G7 post-flip security verification**: DEFERRED — codeql SARIF upload requires Advanced Security (not available for private repos on GitHub Free); branch protection/rulesets 403. Features unlock at authorized visibility switch.
- **G8 publication acknowledgement**: NOT RUN — no visibility authorization.

Full evidence and run IDs in PUBLICATION_EVIDENCE.yaml (authoritative).

**Not publishable until: (1) formal rights review completes (G5), (2) post-flip security
features are verified after an authorized visibility switch (G7-post), and (3) explicit
visibility authorization is granted (G8).**