import pytest
from nora_capabilities.contracts import (
    CapabilityKind,
    CapabilityManifest,
    HumanConfirmationRule,
    PermissionTier,
    TrustState
)

def test_capability_manifest_contracts():
    manifest = CapabilityManifest(
        capability_id="CAP-MCP-SEARCH",
        kind=CapabilityKind.MCP,
        name="Search Legal Database",
        description="Searches case law database",
        permission_tier=PermissionTier.READ_ONLY,
        trust_state=TrustState.AUTHORIZED,
        side_effects=False,
        confirmation_rule=HumanConfirmationRule(requires_approval=False)
    )
    
    assert manifest.kind == CapabilityKind.MCP
    assert manifest.trust_state == TrustState.AUTHORIZED
    assert manifest.permission_tier == PermissionTier.READ_ONLY
    assert manifest.side_effects is False
