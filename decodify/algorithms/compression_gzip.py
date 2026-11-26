
# decodify/algorithms/compression_gzip.py

import base64
import gzip


def encode_gzip(message: str) -> str:
    compressed = gzip.compress(
        message.encode("utf-8"),
        mtime=0
    )
    return base64.b64encode(compressed).decode("ascii")


def decode_gzip(encoded: str) -> str:
    try:
        compressed = base64.b64decode(encoded, validate=True)
        return gzip.decompress(compressed).decode("utf-8")
    except Exception as exc:
        raise ValueError("Invalid GZIP input") from exc


def is_gzip(encoded: str) -> bool:
    try:
        decode_gzip(encoded)
        return True
    except (ValueError, TypeError):
        return False
