import os
import random

def shred_file(file_path: str, passes: int = 3):
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File does not exist.")

    file_size = os.path.getsize(file_path)

    with open(file_path, "ba+", buffering=0) as f:
        for _ in range(passes):
            f.seek(0)
            f.write(os.urandom(file_size))
            f.flush()
            os.fsync(f.fileno())

    os.remove(file_path)
