import base64
import json
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

def pad(data: bytes) -> bytes:
    pad_len = AES.block_size - len(data) % AES.block_size
    return data + bytes([pad_len]) * pad_len

def unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]

def save_encrypted_note(text: str, password: str, file_path: str):
    salt = get_random_bytes(16)
    iv = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32, count=100_000)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(text.encode()))

    vault_data = {
        "salt": base64.b64encode(salt).decode(),
        "iv": base64.b64encode(iv).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode()
    }

    with open(file_path, "w") as f:
        json.dump(vault_data, f, indent=4)

def load_encrypted_note(password: str, file_path: str) -> str:
    with open(file_path, "r") as f:
        data = json.load(f)

    salt = base64.b64decode(data["salt"])
    iv = base64.b64decode(data["iv"])
    ciphertext = base64.b64decode(data["ciphertext"])

    key = PBKDF2(password, salt, dkLen=32, count=100_000)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))

    return plaintext.decode()
