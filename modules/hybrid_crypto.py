import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_aes_key(length=32) -> bytes:
    return get_random_bytes(length)

def encrypt_data_aes(data: str, aes_key: bytes) -> dict:
    cipher = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return {
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "nonce": base64.b64encode(cipher.nonce).decode(),
        "tag": base64.b64encode(tag).decode()
    }

def decrypt_data_aes(encrypted: dict, aes_key: bytes) -> str:
    nonce = base64.b64decode(encrypted["nonce"])
    ciphertext = base64.b64decode(encrypted["ciphertext"])
    tag = base64.b64decode(encrypted["tag"])
    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

def encrypt_aes_key_with_rsa(aes_key: bytes, public_key_pem: str) -> str:
    public_key = serialization.load_pem_public_key(public_key_pem.encode())
    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return base64.b64encode(encrypted_key).decode()

def decrypt_aes_key_with_rsa(encrypted_key_b64: str, private_key_pem: str) -> bytes:
    private_key = serialization.load_pem_private_key(private_key_pem.encode(), password=None)
    encrypted_key = base64.b64decode(encrypted_key_b64)
    return private_key.decrypt(
        encrypted_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

def hybrid_encrypt(plaintext: str, rsa_public_key_pem: str) -> dict:
    aes_key = generate_aes_key()
    encrypted_data = encrypt_data_aes(plaintext, aes_key)
    encrypted_key = encrypt_aes_key_with_rsa(aes_key, rsa_public_key_pem)
    return {
        "encrypted_key": encrypted_key,
        "data": encrypted_data
    }

def hybrid_decrypt(payload: dict, rsa_private_key_pem: str) -> str:
    aes_key = decrypt_aes_key_with_rsa(payload["encrypted_key"], rsa_private_key_pem)
    return decrypt_data_aes(payload["data"], aes_key)

if __name__ == "__main__":
    from modules import asymmetric_rsa

    # Generate temporary RSA keys
    priv, pub = asymmetric_rsa.generate_rsa_keypair()
    priv_pem, pub_pem = asymmetric_rsa.serialize_keys(priv, pub)

    message = "Hybrid encryption test!"

    encrypted_payload = hybrid_encrypt(message, pub_pem)
    print("Encrypted payload:", encrypted_payload)

    decrypted = hybrid_decrypt(encrypted_payload, priv_pem)
    print("Decrypted message:", decrypted)