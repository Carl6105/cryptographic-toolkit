import random

def modexp(base, exp, mod):
    return pow(base, exp, mod)

def simulate_dh_key_exchange() -> list:
    steps = []

    # Prime number and base (small for demo)
    p = 23  # Prime modulus
    g = 5   # Primitive root

    steps.append(f"Public Prime (p): {p}")
    steps.append(f"Public Base (g): {g}")

    # Alice
    a = random.randint(2, p - 2)
    A = modexp(g, a, p)
    steps.append(f"\nAlice's private key (a): {a}")
    steps.append(f"Alice sends A = g^a mod p = {A}")

    # Bob
    b = random.randint(2, p - 2)
    B = modexp(g, b, p)
    steps.append(f"\nBob's private key (b): {b}")
    steps.append(f"Bob sends B = g^b mod p = {B}")

    # Shared secrets
    shared_alice = modexp(B, a, p)
    shared_bob = modexp(A, b, p)

    steps.append(f"\nAlice computes shared key: B^a mod p = {shared_alice}")
    steps.append(f"Bob computes shared key: A^b mod p = {shared_bob}")

    steps.append(f"\nShared Secret Key: {shared_alice}" if shared_alice == shared_bob else "Keys do not match!")

    return steps
