import base64
import binascii

def encode_base64(text: str) -> str:
    return base64.b64encode(text.encode()).decode()

def decode_base64(encoded: str) -> str:
    try:
        return base64.b64decode(encoded.encode()).decode()
    except Exception as e:
        return f"Invalid Base64: {e}"

def encode_hex(text: str) -> str:
    return binascii.hexlify(text.encode()).decode()

def decode_hex(encoded: str) -> str:
    try:
        return binascii.unhexlify(encoded.encode()).decode()
    except Exception as e:
        return f"Invalid Hex: {e}"
