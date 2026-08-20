# Architecture

## Invariants

1. The public repository contains reusable technology, not private Matter data.
2. Every important output has an inspectable basis appropriate to this project's domain.
3. Authorization is evaluated before data is exposed to retrieval/tool/model paths where applicable.
4. Model output is a transformation, not a source of truth.
5. Unknown and disputed states are valid outputs.
6. Tests/evals use synthetic or redistributable fixtures.
7. Migration provenance is explicit.

## Target-specific architecture

CapabilityManifest → source/provenance metadata → trust lifecycle →
policy validation → permission resolution → ExecutionGrant → adapter/compiler.

Lifecycle: discovered → metadata verified → source verified → security reviewed →
sandbox tested → approved → installed → enabled.

## Extension points

MCP adapters, Skill adapters, tool/model/workflow adapters, policy engines, client compilers, sandbox providers.

## Compatibility

Public contracts should be versioned and provider-neutral where practical.

## Architecture decisions

Record consequential changes under `docs/decisions/`.
