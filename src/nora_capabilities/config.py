from __future__ import annotations
from typing import Any, Dict
from nora_capabilities.contracts import CapabilityManifest

class CapabilityConfigRenderer:
    """
    Renders provider configuration blocks while excluding sensitive credentials or private cloud endpoints.
    """
    def render_safe_config(self, manifest: CapabilityManifest) -> Dict[str, Any]:
        raw_meta = dict(manifest.metadata)
        # Redact secrets or private operator URLs
        sanitized_meta = {
            k: ("[REDACTED]" if any(s in k.lower() for s in ["key", "secret", "token", "auth"]) else v)
            for k, v in raw_meta.items()
        }
        
        return {
            "capability_id": manifest.capability_id,
            "name": manifest.name,
            "kind": manifest.kind.value,
            "permission_tier": manifest.permission_tier.value,
            "trust_state": manifest.trust_state.value,
            "configuration": sanitized_meta
        }
