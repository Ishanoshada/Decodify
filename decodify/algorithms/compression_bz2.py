
# decodify/algorithms/compression_bz2.py

import base64
import bz2


def encode_bz2(message: str) -> str:
    compressed = bz2.compress(message.encode("utf-8"))
    return base64.b64encode(compressed).decode("ascii")


def decode_bz2(encoded: str) -> str:
    try:
        compressed = base64.b64decode(encoded, validate=True)
        return bz2.decompress(compressed).decode("utf-8")
    except Exception as exc:
        raise ValueError("Invalid BZ2 input") from exc


def is_bz2(encoded: str) -> bool:
    try:
        decode_bz2(encoded)
        return True
    except (ValueError, TypeError):
        return False
