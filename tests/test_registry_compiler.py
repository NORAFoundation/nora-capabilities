import pytest
from nora_capabilities.compiler import ClientCapabilityCompiler
from nora_capabilities.contracts import CapabilityKind, CapabilityManifest, TrustState
from nora_capabilities.registry import CapabilityRegistry

def test_registry_and_compiler_authorized_flow():
    registry = CapabilityRegistry()
    
    unauth_manifest = CapabilityManifest(
        capability_id="CAP-1",
        kind=CapabilityKind.TOOL,
        name="Unverified Tool",
        description="Dangerous unverified tool",
        trust_state=TrustState.DISCOVERED
    )
    
    auth_manifest = CapabilityManifest(
        capability_id="CAP-2",
        kind=CapabilityKind.TOOL,
        name="Authorized Search",
        description="Audited search tool",
        trust_state=TrustState.AUTHORIZED
    )
    
    registry.register(unauth_manifest)
    registry.register(auth_manifest)
    
    authorized_list = registry.list_authorized()
    assert len(authorized_list) == 1
    assert authorized_list[0].capability_id == "CAP-2"
    
    compiler = ClientCapabilityCompiler()
    
    # Assert unauthorized tool fails compilation
    with pytest.raises(PermissionError):
        compiler.compile_schema(unauth_manifest)
        
    schema = compiler.compile_schema(auth_manifest)
    assert schema["function"]["name"] == "authorized_search"
