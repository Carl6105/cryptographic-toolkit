import hashlib

def file_hash(file_path: str, algorithm: str = "sha256") -> str:
    algo = algorithm.lower()
    if algo not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hasher = hashlib.new(algo)
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()
