
# decodify/algorithms/compression_lzma.py

import base64
import lzma


def encode_lzma(message: str) -> str:
    compressed = lzma.compress(message.encode("utf-8"))
    return base64.b64encode(compressed).decode("ascii")


def decode_lzma(encoded: str) -> str:
    try:
        compressed = base64.b64decode(encoded, validate=True)
        return lzma.decompress(compressed).decode("utf-8")
    except Exception as exc:
        raise ValueError("Invalid LZMA input") from exc


def is_lzma(encoded: str) -> bool:
    try:
        decode_lzma(encoded)
        return True
    except (ValueError, TypeError):
        return False
