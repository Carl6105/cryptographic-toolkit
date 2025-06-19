import jwt
from jwt import PyJWTError
from typing import Literal
import base64

def create_jwt(payload: dict, key: str, algorithm: Literal["HS256", "RS256", "ES256"]) -> str:
    return jwt.encode(payload, key, algorithm=algorithm)

def verify_jwt(token: str, key: str, algorithm: Literal["HS256", "RS256", "ES256"]) -> dict:
    try:
        decoded = jwt.decode(token, key, algorithms=[algorithm])
        return {"valid": True, "payload": decoded}
    except PyJWTError as e:
        return {"valid": False, "error": str(e)}
