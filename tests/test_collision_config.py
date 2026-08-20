import pytest
from nora_capabilities.collision import CapabilityCollisionResolver
from nora_capabilities.config import CapabilityConfigRenderer
from nora_capabilities.contracts import CapabilityKind, CapabilityManifest, PermissionTier, TrustState

def test_collision_resolver_and_config_renderer():
    m1 = CapabilityManifest(
        capability_id="CAP-DUP",
        kind=CapabilityKind.TOOL,
        name="Search Tool",
        version="0.0.1"
    )
    
    m2 = CapabilityManifest(
        capability_id="CAP-DUP",
        kind=CapabilityKind.TOOL,
        name="Search Tool",
        version="0.0.2"
    )
    
    resolver = CapabilityCollisionResolver()
    resolved = resolver.resolve_collision(m1, m2)
    assert resolved.version == "0.0.2"
    
    m_secret = CapabilityManifest(
        capability_id="CAP-SECRET",
        kind=CapabilityKind.MCP,
        name="MCP Private Tool",
        permission_tier=PermissionTier.HIGH_RISK_ADMIN,
        trust_state=TrustState.AUTHORIZED,
        metadata={"api_key": "secret_token_val_123", "endpoint": "https://api.public.org"}
    )
    
    renderer = CapabilityConfigRenderer()
    config = renderer.render_safe_config(m_secret)
    
    assert config["configuration"]["api_key"] == "[REDACTED]"
    assert config["configuration"]["endpoint"] == "https://api.public.org"
