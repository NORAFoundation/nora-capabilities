# ADR-0001: Universal Capability Manifest and Trust Lifecycle

- **Status:** Accepted
- **Date:** 2026-08-19
- **Deciders:** NORA Foundation Engineering Team

## Context

Capabilities (MCP tools, Skills, workflows, models) require provider-neutral, least-privilege governance (`AGENTS.md`, `policies/LICENSE_AND_PROVENANCE.md`).

## Decision

We adopt strict governance invariants:
1. **Discovery != Authorization:** Discovering an MCP tool or Skill registers it in state `DISCOVERED`; execution requires state `AUTHORIZED`.
2. **Explicit Permission Tiers:** Every capability declares a `PermissionTier` (`READ_ONLY`, `SIDE_EFFECT_MUTATING`, `HIGH_RISK_ADMIN`).
3. **Side Effect & Human Approval:** Mutating or external side-effect tools enforce `HumanConfirmationRule`.

## Consequences

- No silent capability promotion: tools are untrusted until explicitly audited and authorized.
- Clear separation between capability discovery, audit, authorization, and execution.
