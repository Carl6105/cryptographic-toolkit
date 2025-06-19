from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
import base64

def generate_ecc_keypair():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    return private_key, public_key

def serialize_ecc_keys(private_key, public_key):
    priv_bytes = private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption()
    )
    pub_bytes = public_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return priv_bytes.decode(), pub_bytes.decode()

def sign_ecc_message(private_key_pem: str, message: str) -> str:
    private_key = serialization.load_pem_private_key(private_key_pem.encode(), password=None)
    signature = private_key.sign(message.encode(), ec.ECDSA(hashes.SHA256()))
    return base64.b64encode(signature).decode()

def verify_ecc_signature(public_key_pem: str, message: str, signature_b64: str) -> bool:
    public_key = serialization.load_pem_public_key(public_key_pem.encode())
    try:
        public_key.verify(base64.b64decode(signature_b64), message.encode(), ec.ECDSA(hashes.SHA256()))
        return True
    except Exception:
        return False
