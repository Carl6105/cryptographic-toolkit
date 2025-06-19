import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa, ec
from cryptography.exceptions import InvalidSignature

def load_private_key(pem_data: str, algorithm: str):
    private_key = serialization.load_pem_private_key(
        pem_data.encode(),
        password=None,
    )
    return private_key

def load_public_key(pem_data: str, algorithm: str):
    public_key = serialization.load_pem_public_key(
        pem_data.encode()
    )
    return public_key

def sign_file(file_path: str, private_key_pem: str, algorithm: str = "RSA") -> str:
    with open(file_path, "rb") as f:
        data = f.read()

    private_key = load_private_key(private_key_pem, algorithm)

    if algorithm.upper() == "RSA":
        signature = private_key.sign(
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
    elif algorithm.upper() == "ECC":
        signature = private_key.sign(
            data,
            ec.ECDSA(hashes.SHA256())
        )
    else:
        raise ValueError("Unsupported algorithm")

    return base64.b64encode(signature).decode()

def verify_file_signature(file_path: str, signature_b64: str, public_key_pem: str, algorithm: str = "RSA") -> bool:
    with open(file_path, "rb") as f:
        data = f.read()

    public_key = load_public_key(public_key_pem, algorithm)
    signature = base64.b64decode(signature_b64)

    try:
        if algorithm.upper() == "RSA":
            public_key.verify(
                signature,
                data,
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        elif algorithm.upper() == "ECC":
            public_key.verify(
                signature,
                data,
                ec.ECDSA(hashes.SHA256())
            )
        else:
            raise ValueError("Unsupported algorithm")
        return True
    except InvalidSignature:
        return False
