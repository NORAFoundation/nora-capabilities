from __future__ import annotations
from typing import Any, Dict, List
from nora_capabilities.contracts import CapabilityManifest, TrustState

class ClientCapabilityCompiler:
    """
    Compiles authorized capability manifests into provider-agnostic tool schemas.
    """
    def compile_schema(self, manifest: CapabilityManifest) -> Dict[str, Any]:
        if manifest.trust_state != TrustState.AUTHORIZED:
            raise PermissionError(f"Cannot compile unauthorized capability {manifest.capability_id}")

        return {
            "type": "function",
            "function": {
                "name": manifest.name.replace(" ", "_").lower(),
                "description": manifest.description,
                "parameters": {
                    "type": "object",
                    "properties": manifest.metadata.get("parameters", {}),
                    "required": manifest.metadata.get("required", [])
                }
            }
        }
