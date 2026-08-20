from __future__ import annotations
from typing import Dict, List, Optional
from nora_capabilities.contracts import CapabilityManifest

class CapabilityCollisionResolver:
    """
    Detects and resolves naming or ID collisions across registered capabilities
    (derived from agent-control-plane).
    """
    def resolve_collision(self, existing: CapabilityManifest, incoming: CapabilityManifest) -> CapabilityManifest:
        if existing.capability_id == incoming.capability_id:
            # Higher version or explicit override resolution
            if incoming.version > existing.version:
                return incoming
            return existing
        
        # Name collision handling
        if existing.name.lower() == incoming.name.lower():
            incoming.name = f"{incoming.name} ({incoming.capability_id})"
            
        return incoming
