import hashlib

def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def bit_difference(hash1: str, hash2: str) -> int:
    b1 = bin(int(hash1, 16))[2:].zfill(256)
    b2 = bin(int(hash2, 16))[2:].zfill(256)
    return sum(c1 != c2 for c1, c2 in zip(b1, b2))

def simulate_avalanche(text1: str, text2: str) -> dict:
    h1 = sha256_hash(text1)
    h2 = sha256_hash(text2)
    diff = bit_difference(h1, h2)

    return {
        "hash1": h1,
        "hash2": h2,
        "bit_diff": diff
    }
