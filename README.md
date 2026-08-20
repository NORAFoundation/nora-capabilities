# nora-capabilities

Provider-neutral capability governance for MCP servers, Skills, tools, agents, workflows, models, and packs.

**Status:** pre-alpha / migration build

## Hard problem

Discover many tools/Skills/MCP servers/agents/workflows without confusing discovery with trust, permission or execution authority.

## Why this exists

This repository isolates one reusable public-interest technology problem from the NORA Foundation platform so developers and researchers can improve it independently.

## Minimum vertical slice

manifest load -> trust validation -> permission grant -> bounded execution descriptor -> two client adapters

## Non-goals

- NORA One product UI
- private Matter storage
- generic SaaS dashboard work
- autonomous legal advice
- publication of private source corpora
- claims of production readiness without release evidence

## Quick start

```bash
make doctor
make validate
make test
```

## Source provenance

Legacy NORA repositories are component sources, not authorities. Migrated units are recorded in `SOURCE_PROVENANCE.yaml`.

## Contributing

See `CONTRIBUTING.md` and `ROADMAP.md`.

## Security

See `SECURITY.md`.

## License

New clean-room code is Apache-2.0. Migrated/third-party material remains subject to its recorded source license and notices.
