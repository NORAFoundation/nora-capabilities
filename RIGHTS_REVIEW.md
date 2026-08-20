# Rights / Provenance Review Register — nora-capabilities

**Gate:** G5 (licensing/provenance) — **STATUS: BLOCKED**

Formal external rights/provenance review is outstanding for every entry below.
This register is the durable record of each unresolved item. It is **not** a
resolution of any legal/rights question; no item below may be treated as cleared
until a named reviewer records a decision.

| ID | Source repo / commit / lineage | Source path(s) | Why review required | License / rights question | Evidence already collected | Required reviewer / decision | Remediation if rejected | Publication impact |
|----|-------------------------------|----------------|---------------------|---------------------------|---------------------------|------------------------------|-------------------------|--------------------|
| PROV-CAP-001 | `NORA-BITSY/nora-agent-platform` @ `43aea342` (Unlicensed) | `src/capabilities/registry.py`, `src/capabilities/compiler.py` → `src/nora_capabilities/registry.py`, `src/nora_capabilities/compiler.py` | Unlicensed internal monorepo package relicensed Apache-2.0; explicit sign-off required. | Was relicensing authorized? Any third-party code embedded in extracted modules? | SOURCE_PROVENANCE.yaml entry; secret/privacy/license scan pass (agent-level); `authorization_reference: INTERNAL_CLEANROOM_TRANSPLANT_PENDING_EXPLICIT_SIGN_OFF` | Named human reviewer with relicensing authority. | Re-derive/replace extracted modules; re-run gates. | Blocks publication of nora-capabilities (hard blocker per G5). |
| PROV-CAP-002 | `NORA-BITSY/agent-control-plane` @ `69e120aa` (NOASSERTION) | `src/control/collision.py`, `src/control/config.py` → `src/nora_capabilities/collision.py`, `src/nora_capabilities/config.py` | Original license recorded as NOASSERTION; patterns extracted and relicensed Apache-2.0. | Is NOASSERTION source acceptable for relicensing? Any private operator/cloud endpoints leaked (extraction excluded them — verify)? | SOURCE_PROVENANCE.yaml entry; secret/privacy/license scan pass (agent-level); changes note "Excluded private operator and cloud endpoints"; `authorization_reference: INTERNAL_CLEANROOM_TRANSPLANT_PENDING_EXPLICIT_SIGN_OFF` | Named human reviewer; NOASSERTION source disposition decision. | Replace or re-derive affected patterns; re-run gates. | Blocks publication of nora-capabilities (hard blocker per G5). |

**Rights review pending items (inherited from evidence file):**
- Canon licensing/version compatibility: confirm any Canon-referenced material is
  license-compatible with Apache-2.0 target.
- Synthetic redaction fixtures in history are asserted `[REDACTED]` by design (secret
  scan "matches" are intentional fixture values — no real secrets).

**Status line (required closeout language):**
Technical publication preparation complete. Formal rights/provenance review remains
outstanding. Repository remains private. No visibility authorization has been granted.