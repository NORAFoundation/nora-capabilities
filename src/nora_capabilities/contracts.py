from __future__ import annotations
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Set
from pydantic import BaseModel, Field

class PermissionTier(str, Enum):
    READ_ONLY = "read_only"
    SIDE_EFFECT_MUTATING = "side_effect_mutating"
    HIGH_RISK_ADMIN = "high_risk_admin"

class TrustState(str, Enum):
    DISCOVERED = "discovered"
    AUDITED = "audited"
    AUTHORIZED = "authorized"
    REVOKED = "revoked"

class CapabilityKind(str, Enum):
    MCP = "mcp"
    SKILL = "skill"
    TOOL = "tool"
    WORKFLOW = "workflow"
    MODEL = "model"

class HumanConfirmationRule(BaseModel):
    requires_approval: bool = False
    approval_prompt: Optional[str] = None
    risk_level: str = "low"

class CapabilityManifest(BaseModel):
    capability_id: str
    kind: CapabilityKind
    name: str
    version: str = "0.0.1"
    description: str
    permission_tier: PermissionTier = PermissionTier.READ_ONLY
    trust_state: TrustState = TrustState.DISCOVERED
    side_effects: bool = False
    allowed_data_classes: Set[str] = Field(default_factory=lambda: {"public"})
    confirmation_rule: HumanConfirmationRule = Field(default_factory=HumanConfirmationRule)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    registered_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
