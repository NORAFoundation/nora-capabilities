import pytest
from nora_capabilities.collision import CapabilityCollisionResolver
from nora_capabilities.compiler import ClientCapabilityCompiler
from nora_capabilities.config import CapabilityConfigRenderer
from nora_capabilities.contracts import (
    CapabilityKind,
    CapabilityManifest,
    HumanConfirmationRule,
    PermissionTier,
    TrustState
)
from nora_capabilities.registry import CapabilityRegistry
from nora_capabilities.trust import TrustLifecycleValidator

def test_nora_capabilities_minimum_vertical_slice():
    """
    Minimum Vertical Slice:
    manifest -> trust validation -> permission grant -> client compilation -> safe config rendering
    """
    # 1. Create capability manifest
    manifest = CapabilityManifest(
        capability_id="CAP-SYNTHETIC-001",
        kind=CapabilityKind.MCP,
        name="Synthetic Search Capability",
        description="Audited synthetic search capability for evaluation",
        permission_tier=PermissionTier.READ_ONLY,
        trust_state=TrustState.DISCOVERED,
        metadata={"api_key": "secret_token_val_999", "timeout": 30}
    )

    # 2. Register capability
    registry = CapabilityRegistry()
    registry.register(manifest)

    # 3. Trust lifecycle transition: DISCOVERED -> AUDITED -> AUTHORIZED
    validator = TrustLifecycleValidator()
    v1, _ = validator.validate_transition(manifest, TrustState.AUDITED)
    assert v1 is True
    manifest.trust_state = TrustState.AUDITED

    v2, _ = validator.validate_transition(manifest, TrustState.AUTHORIZED)
    assert v2 is True
    manifest.trust_state = TrustState.AUTHORIZED

    # 4. Compile client schemas (OpenAI / Anthropic style function schema)
    compiler = ClientCapabilityCompiler()
    schema = compiler.compile_schema(manifest)
    assert schema["type"] == "function"
    assert schema["function"]["name"] == "synthetic_search_capability"

    # 5. Render safe configuration (excluding secrets)
    config_renderer = CapabilityConfigRenderer()
    safe_config = config_renderer.render_safe_config(manifest)
    assert safe_config["configuration"]["api_key"] == "[REDACTED]"
    assert safe_config["configuration"]["timeout"] == 30
