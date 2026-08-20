from __future__ import annotations
from typing import Dict, List, Optional
from nora_capabilities.contracts import CapabilityManifest, TrustState

class CapabilityRegistry:
    """
    Registry for MCP servers, Skills, tools, workflows, and models harvested
    from nora-agent-platform.
    """
    def __init__(self):
        self._capabilities: Dict[str, CapabilityManifest] = {}

    def register(self, manifest: CapabilityManifest) -> None:
        self._capabilities[manifest.capability_id] = manifest

    def get(self, capability_id: str) -> Optional[CapabilityManifest]:
        return self._capabilities.get(capability_id)

    def list_authorized(self) -> List[CapabilityManifest]:
        return [c for c in self._capabilities.values() if c.trust_state == TrustState.AUTHORIZED]

    def list_all(self) -> List[CapabilityManifest]:
        return list(self._capabilities.values())
