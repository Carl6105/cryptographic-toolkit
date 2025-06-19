import base64
import json

def pad_base64(b64: str) -> str:
    return b64 + '=' * ((4 - len(b64) % 4) % 4)

def decode_jwt(token: str) -> dict:
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return {"error": "Invalid JWT format (must have 3 parts)"}

        header_b64, payload_b64, signature_b64 = parts

        header = json.loads(base64.urlsafe_b64decode(pad_base64(header_b64)).decode())
        payload = json.loads(base64.urlsafe_b64decode(pad_base64(payload_b64)).decode())

        return {
            "header": header,
            "payload": payload,
            "signature": signature_b64
        }

    except Exception as e:
        return {"error": str(e)}

def tamper_jwt(original_token: str, new_payload: dict) -> str:
    try:
        parts = original_token.split(".")
        if len(parts) != 3:
            raise ValueError("Invalid JWT format")

        header_b64 = parts[0]

        new_payload_json = json.dumps(new_payload, separators=(",", ":")).encode()
        new_payload_b64 = base64.urlsafe_b64encode(new_payload_json).decode().rstrip("=")

        # Note: Signature is omitted (unsigned tampered JWT)
        return f"{header_b64}.{new_payload_b64}."

    except Exception as e:
        return f"Error: {str(e)}"
