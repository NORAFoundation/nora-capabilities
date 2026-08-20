#!/usr/bin/env python3
"""nora-capabilities demo: manifest -> trust lifecycle -> permission grant -> client compilation.

Run:  python examples/demo.py
"""
from __future__ import annotations

from nora_capabilities.collision import CapabilityCollisionResolver
from nora_capabilities.compiler import ClientCapabilityCompiler
from nora_capabilities.config import CapabilityConfigRenderer
from nora_capabilities.contracts import (
    CapabilityKind,
    CapabilityManifest,
    PermissionTier,
    TrustState,
)
from nora_capabilities.registry import CapabilityRegistry
from nora_capabilities.trust import TrustLifecycleValidator


def main() -> None:
    print("nora-capabilities — capability governance demo")
    print("=" * 48)

    # 1. Create capability manifest.
    manifest = CapabilityManifest(
        capability_id="CAP-SYNTHETIC-001",
        kind=CapabilityKind.MCP,
        name="Synthetic Search Capability",
        description="Audited synthetic search capability for evaluation",
        permission_tier=PermissionTier.READ_ONLY,
        trust_state=TrustState.DISCOVERED,
        metadata={"api_key": "secret_token_val_999", "timeout": 30},
    )
    print(f"  \u2713 Manifest loaded ({manifest.capability_id}, {manifest.kind.value})")

    # 2. Register + collision handling (same ID, higher version wins).
    registry = CapabilityRegistry()
    registry.register(manifest)
    duplicate = CapabilityManifest(
        capability_id="CAP-SYNTHETIC-001",
        kind=CapabilityKind.MCP,
        name="Synthetic Search Capability",
        description="Duplicate with newer version",
        version="0.0.2",
    )
    collision = CapabilityCollisionResolver()
    resolved = collision.resolve_collision(manifest, duplicate)
    print(f"  \u2713 Collision resolved (version {resolved.version} wins)")
    print("  \u2713 Trust validated (DISCOVERED -> AUDITED -> AUTHORIZED)")

    # 3. Trust lifecycle transition.
    validator = TrustLifecycleValidator()
    v1, _ = validator.validate_transition(manifest, TrustState.AUDITED)
    manifest.trust_state = TrustState.AUDITED
    v2, _ = validator.validate_transition(manifest, TrustState.AUTHORIZED)
    manifest.trust_state = TrustState.AUTHORIZED
    print(f"  \u2713 Permissions granted ({manifest.permission_tier.value}, "
          f"state: {manifest.trust_state.value})")

    # 4. Compile client schema.
    compiler = ClientCapabilityCompiler()
    schema = compiler.compile_schema(manifest)
    print(f"  \u2713 Execution descriptors compiled "
          f"({schema['function']['name']}, {schema['type']})")

    # 5. Render safe configuration (secrets redacted).
    renderer = CapabilityConfigRenderer()
    safe = renderer.render_safe_config(manifest)
    redacted_ok = safe["configuration"]["api_key"] == "[REDACTED]"
    print(f"  \u2713 Secret redacted in rendered config: {redacted_ok}")

    print("=" * 48)
    if not (v1 and v2 and redacted_ok and resolved.version == "0.0.2"):
        raise SystemExit("Demo failed: capability invariants not satisfied.")
    print("Demo PASS — capabilities governed, trusted, and safely rendered.")


if __name__ == "__main__":
    main()