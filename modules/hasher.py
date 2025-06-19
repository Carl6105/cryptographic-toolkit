import hashlib
import base64
from typing import Literal

HashAlgo = Literal["md5", "sha1", "sha256", "sha512"]

def hash_string(data: str, algorithm: HashAlgo = "sha256", base64_output: bool = False) -> str:
    algo = getattr(hashlib, algorithm)()
    algo.update(data.encode('utf-8'))
    digest = algo.digest()
    return base64.b64encode(digest).decode() if base64_output else algo.hexdigest()

def hash_file(file_path: str, algorithm: HashAlgo = "sha256", base64_output: bool = False) -> str:
    algo = getattr(hashlib, algorithm)()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            algo.update(chunk)
    digest = algo.digest()
    return base64.b64encode(digest).decode() if base64_output else algo.hexdigest()

def get_supported_algorithms() -> list[str]:
    return ["md5", "sha1", "sha256", "sha512"]
