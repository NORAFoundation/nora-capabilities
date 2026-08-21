"""nora-capabilities package."""

from .collision import CapabilityCollisionResolver
from .compiler import ClientCapabilityCompiler
from .config import CapabilityConfigRenderer
from .contracts import (
    CapabilityKind,
    CapabilityManifest,
    HumanConfirmationRule,
    PermissionTier,
    TrustState,
)
from .registry import CapabilityRegistry
from .trust import TrustLifecycleValidator

__all__ = [
    "CapabilityCollisionResolver",
    "CapabilityKind",
    "CapabilityManifest",
    "CapabilityRegistry",
    "CapabilityConfigRenderer",
    "ClientCapabilityCompiler",
    "HumanConfirmationRule",
    "PermissionTier",
    "TrustLifecycleValidator",
    "TrustState",
]
__version__ = "0.0.1"
