# Current State — nora-capabilities

**Status:** OSS EXTRACTION / RECONCILIATION IN PROGRESS
**Version:** 0.0.1

## Implemented Reference Slice

The minimum reference vertical slice is complete and verified:
`manifest -> trust -> permission grant -> execution descriptor -> client adapters`

- `src/nora_capabilities/contracts.py`: Dataclasses for `CapabilityManifest`, `PermissionTier`, `TrustState`, `CapabilityKind`, and `HumanConfirmationRule`.
- `src/nora_capabilities/registry.py`: `CapabilityRegistry` managing MCP tools, Skills, workflows, and models.
- `src/nora_capabilities/compiler.py`: `ClientCapabilityCompiler` generating client tool function schemas.
- `src/nora_capabilities/collision.py`: `CapabilityCollisionResolver` handling version and naming collisions.
- `src/nora_capabilities/config.py`: `CapabilityConfigRenderer` sanitizing sensitive credentials and private cloud parameters.
- `src/nora_capabilities/trust.py`: `TrustLifecycleValidator` enforcing least-privilege audit and authorization constraints.
## Contract Targets — Not Yet Implemented

The following symbols are defined in broader specifications but have no implementation in the current codebase:

- `CapabilityAdapter` — generic adapter for external capability providers (e.g., cloud services)
- `MCPIntegration` — integration layer with the NORA Agent Platform for dynamic capability discovery
- `ToolBackend` — runtime execution backend for tool commands (currently only CLI stub)

## Verified

- `make test` / `pytest`: **6 passed in 0.12s**.
- Vertical-slice test path: `tests/test_vertical_slice.py`.
- End-to-end capability manifest registration, trust transition, client schema compilation, and safe config rendering verified.

## Not Yet Established

- canonical feature parity;
- public extraction completeness;
- production deployment status;
- resolution of unlicensed internal lineage (`nora-agent-platform` / `agent-control-plane`).
