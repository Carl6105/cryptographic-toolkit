from typing import Literal
import base64

from Crypto.Protocol.KDF import PBKDF2, scrypt
from cryptography.hazmat.primitives.kdf.argon2 import Argon2
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

import os

def derive_key_pbkdf2(password: str, salt: bytes, length: int = 32, iterations: int = 100_000) -> bytes:
    return PBKDF2(password, salt, dkLen=length, count=iterations)

def derive_key_scrypt(password: str, salt: bytes, length: int = 32) -> bytes:
    return scrypt(password, salt=salt, key_len=length, N=2**14, r=8, p=1)

def derive_key_argon2(password: str, salt: bytes, length: int = 32) -> bytes:
    kdf = Argon2(
        memory_cost=65536,
        time_cost=4,
        parallelism=2,
        length=length,
        salt=salt,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def generate_salt(length: int = 16) -> bytes:
    return os.urandom(length)

def key_to_base64(key: bytes) -> str:
    return base64.b64encode(key).decode()

def get_supported_kdfs() -> list[str]:
    return ["PBKDF2", "Scrypt", "Argon2"]

if __name__ == "__main__":
    pwd = "supersecure"
    salt = generate_salt()

    k1 = derive_key_pbkdf2(pwd, salt)
    k2 = derive_key_scrypt(pwd, salt)
    k3 = derive_key_argon2(pwd, salt)

    print("PBKDF2:", key_to_base64(k1))
    print("Scrypt :", key_to_base64(k2))
    print("Argon2 :", key_to_base64(k3))