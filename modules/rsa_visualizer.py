from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def simulate_rsa_keygen() -> dict:
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    private_numbers = private_key.private_numbers()
    public_numbers = private_key.public_key().public_numbers()

    rsa_info = {
        "Modulus (n)": hex(public_numbers.n),
        "Public Exponent (e)": hex(public_numbers.e),
        "Private Exponent (d)": hex(private_numbers.d),
        "Prime 1 (p)": hex(private_numbers.p),
        "Prime 2 (q)": hex(private_numbers.q)
    }

    return rsa_info
