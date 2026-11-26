# decodify/algorithms/rot13.py
import codecs

def is_rot13(encoded: str) -> bool:
    """Weak cipher – detection disabled; user must specify algorithm."""
    return False
    letters = sum(1 for c in encoded if c.isalpha())
    return letters / max(len(encoded), 1) > 0.5

def decode_rot13(encoded: str) -> str:
    """
    Decode (or encode) ROT13.
    """
    return codecs.decode(encoded, "rot_13")

def encode_rot13(message: str) -> str:
    """
    Encode with ROT13 (same as decode).
    """
    return codecs.encode(message, "rot_13")
