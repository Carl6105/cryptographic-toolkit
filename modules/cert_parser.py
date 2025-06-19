from cryptography import x509
from cryptography.hazmat.backends import default_backend

def parse_certificate(pem_data: str) -> dict:
    try:
        cert = x509.load_pem_x509_certificate(pem_data.encode(), default_backend())

        info = {
            "Subject": cert.subject.rfc4514_string(),
            "Issuer": cert.issuer.rfc4514_string(),
            "Serial Number": hex(cert.serial_number),
            "Valid From": cert.not_valid_before.strftime("%Y-%m-%d %H:%M:%S"),
            "Valid Until": cert.not_valid_after.strftime("%Y-%m-%d %H:%M:%S"),
            "Public Key Algorithm": cert.public_key().__class__.__name__,
            "Signature Algorithm": cert.signature_hash_algorithm.name.upper(),
        }

        return info
    except Exception as e:
        return {"error": str(e)}
