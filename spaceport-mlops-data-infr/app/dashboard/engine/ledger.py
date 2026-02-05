import hashlib
import json
from datetime import datetime

class ImmutableLedger:
    """Deterministic Cryptographic Ledger."""
    
    @staticmethod
    def create_block(asset_id: str, action: str, payload: dict, prev_hash: str = "0000") -> dict:
        ts = datetime.utcnow().isoformat()
        
        block_content = {
            "asset_id": asset_id,
            "action": action,
            "data": payload,
            "timestamp": ts,
            "prev_hash_ref": prev_hash,
            "salt": "STATIC_ENTERPRISE_KEY_V1" # Deterministic Salt
        }
        
        # Sort keys ensures identical hash for identical data
        canonical_str = json.dumps(block_content, sort_keys=True)
        block_hash = hashlib.sha256(canonical_str.encode('utf-8')).hexdigest()
        
        return {
            "timestamp": ts,
            "hash": block_hash,
            "content": block_content
        }