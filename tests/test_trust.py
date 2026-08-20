import pytest
from nora_capabilities.contracts import (
    CapabilityKind,
    CapabilityManifest,
    HumanConfirmationRule,
    PermissionTier,
    TrustState
)
from nora_capabilities.trust import TrustLifecycleValidator

def test_trust_lifecycle_validator():
    validator = TrustLifecycleValidator()
    
    m_discovered = CapabilityManifest(
        capability_id="CAP-MCP-1",
        kind=CapabilityKind.MCP,
        name="MCP Data Fetcher",
        description="Fetches data",
        permission_tier=PermissionTier.READ_ONLY,
        trust_state=TrustState.DISCOVERED
    )
    
    valid, note = validator.validate_transition(m_discovered, TrustState.AUDITED)
    assert valid is True
    assert "Audit passed" in note
    
    # HIGH_RISK_ADMIN without human confirmation fails authorization
    m_admin = CapabilityManifest(
        capability_id="CAP-ADMIN-1",
        kind=CapabilityKind.TOOL,
        name="Root Shell Tool",
        description="Executes shell commands",
        permission_tier=PermissionTier.HIGH_RISK_ADMIN,
        trust_state=TrustState.AUDITED,
        confirmation_rule=HumanConfirmationRule(requires_approval=False)
    )
    
    valid, note = validator.validate_transition(m_admin, TrustState.AUTHORIZED)
    assert valid is False
    assert "human approval" in note
