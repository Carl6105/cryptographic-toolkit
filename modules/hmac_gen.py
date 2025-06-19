import hmac
import hashlib
import base64

def generate_hmac(message: str, key: str, algorithm: str = "sha256", base64_output: bool = False) -> str:
    key_bytes = key.encode()
    message_bytes = message.encode()
    digestmod = getattr(hashlib, algorithm)
    hmac_digest = hmac.new(key_bytes, message_bytes, digestmod).digest()
    return base64.b64encode(hmac_digest).decode() if base64_output else hmac_digest.hex()
