import base64

def b64encode(data: bytes) -> str:
    return base64.b64encode(data).decode()

def b64decode(data_b64: str) -> bytes:
    return base64.b64decode(data_b64)

def is_base64(s: str) -> bool:
    try:
        return base64.b64encode(base64.b64decode(s)).decode() == s
    except Exception:
        return False
