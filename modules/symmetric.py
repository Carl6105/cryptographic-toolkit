from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import base64
import os

def derive_key(password: str, salt: bytes, key_length: int = 32) -> bytes:
    return PBKDF2(password, salt, dkLen=key_length, count=100_000)

def encrypt_aes(plaintext: str, password: str) -> dict:
    salt = get_random_bytes(16)
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    return {
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "nonce": base64.b64encode(cipher.nonce).decode(),
        "tag": base64.b64encode(tag).decode(),
        "salt": base64.b64encode(salt).decode(),
    }

def decrypt_aes(data: dict, password: str) -> str:
    try:
        salt = base64.b64decode(data["salt"])
        key = derive_key(password, salt)
        nonce = base64.b64decode(data["nonce"])
        ciphertext = base64.b64decode(data["ciphertext"])
        tag = base64.b64decode(data["tag"])
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode()
    except Exception as e:
        return f"[Decryption Failed] {str(e)}"
