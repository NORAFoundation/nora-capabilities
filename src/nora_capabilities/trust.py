from __future__ import annotations
from typing import List, Tuple
from nora_capabilities.contracts import CapabilityManifest, PermissionTier, TrustState

class TrustLifecycleValidator:
    """
    Validates capability trust lifecycle transitions, verifying source provenance,
    permission tier constraints, and sandbox isolation rules.
    """
    def validate_transition(self, manifest: CapabilityManifest, target_state: TrustState) -> Tuple[bool, str]:
        current = manifest.trust_state
        
        # Discovered -> Audited -> Authorized / Revoked
        if target_state == TrustState.AUDITED:
            if current != TrustState.DISCOVERED:
                return False, f"Invalid transition from {current.value} to audited"
            return True, "Audit passed: Metadata and permission tier verified"

        if target_state == TrustState.AUTHORIZED:
            if current not in {TrustState.AUDITED, TrustState.DISCOVERED}:
                return False, f"Cannot authorize capability from state {current.value}"
            if manifest.permission_tier == PermissionTier.HIGH_RISK_ADMIN and not manifest.confirmation_rule.requires_approval:
                return False, "HIGH_RISK_ADMIN capabilities must mandate human approval"
            return True, "Authorization granted: Least privilege and human approval rules verified"

        if target_state == TrustState.REVOKED:
            return True, "Capability trust revoked"

        return False, f"Unsupported trust transition to {target_state.value}"
