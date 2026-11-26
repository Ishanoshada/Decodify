
# decodify/algorithms/compression_zlib.py

import base64
import zlib


def encode_zlib(message: str) -> str:
    compressed = zlib.compress(message.encode("utf-8"))
    return base64.b64encode(compressed).decode("ascii")


def decode_zlib(encoded: str) -> str:
    try:
        compressed = base64.b64decode(encoded, validate=True)
        return zlib.decompress(compressed).decode("utf-8")
    except Exception as exc:
        raise ValueError("Invalid ZLIB input") from exc


def is_zlib(encoded: str) -> bool:
    try:
        decode_zlib(encoded)
        return True
    except (ValueError, TypeError):
        return False
