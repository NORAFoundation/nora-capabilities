# Rights / Provenance Review Register — nora-capabilities

**Gate:** G5 (licensing/provenance) — **STATUS: BLOCKED**

**Review executed 2026-08-20.** Every lineage entry below received an evidence-based disposition
(verified via GitHub API commit/license checks, candidate git-history searches, and harvest-commit
file inspection). BLOCKED entries may not be treated as cleared until a named human reviewer
records a decision. This register is the durable record.

## Verification record (2026-08-20)

- Source commits checked with `gh api repos/{owner}/{repo}/commits/{sha}`.
- Source licenses checked with `gh api repos/{owner}/{repo}/license` and by reading the top-level
  file listing.
- Contamination search (`git log --all -S`) across this repo for: RAGEmbed, Meridian-Canon,
  NECCL, nora-canon, blakeox, legal-mcp, LawLLama, CC BY-NC, courtlistener-mcp, mcro-mcp,
  agent-canon → **0 hits** (no Canon-referenced material entered this repo's history).
- Harvested files inspected at harvest commits (`git show 3bef7af`, `git show 50fac9e`): small
  derived implementations importing `nora_capabilities` contracts, docstring-attributed to sources;
  not verbatim copies. No vendor directories.
- Evidence artifacts: `/tmp/g5deep.log`, `/tmp/g5verify.log`, `/tmp/g5ev_nora-capabilities.log`.

## Dispositions

| ID | Source repo / commit | Source → target | License verification (2026-08-20) | Disposition | Required reviewer / decision |
|----|----------------------|-----------------|-----------------------------------|-------------|------------------------------|
| PROV-CAP-001 | `NORA-BITSY/nora-agent-platform` @ `43aea342` | `src/capabilities/registry.py`, `src/capabilities/compiler.py` → `src/nora_capabilities/registry.py`, `src/nora_capabilities/compiler.py` | Commit **EXISTS**. Source repo has **no LICENSE file**. | **BLOCKED — RIGHTS UNCLEAR** (unlicensed internal package relicensed Apache-2.0; sign-off required) | Named human reviewer: relicensing sign-off |
| PROV-CAP-002 | `NORA-BITSY/agent-control-plane` @ `69e120aa` | `src/control/collision.py`, `src/control/config.py` → `src/nora_capabilities/collision.py`, `src/nora_capabilities/config.py` | Commit **DOES NOT EXIST** (GitHub 422 "No commit found"). Source repo has **no LICENSE file**. | **BLOCKED — SOURCE UNKNOWN** (recorded commit is a placeholder; NOASSERTION claim unverifiable) | Named human reviewer: pin real source commit + license, or authorize independent re-derivation |

## Rights review pending items (2026-08-20)

- Canon compatibility: contamination search found **no Canon-referenced material** in history;
  the Canon licensing/version-compatibility concern is resolved for this candidate at the
  contamination level.
- agent-platform (PROV-CAP-001) and agent-control-plane (PROV-CAP-002): neither source repo
  carries a license file; the latter's recorded commit does not exist on GitHub.

**Status line (required closeout language):**
G5 rights/provenance review executed 2026-08-20 — **result: BLOCKED** (0/2 lineages clear).
Repository remains private. No visibility authorization has been granted.
**NOT READY FOR PUBLICATION — G5 RIGHTS/PROVENANCE BLOCKERS REMAIN.**