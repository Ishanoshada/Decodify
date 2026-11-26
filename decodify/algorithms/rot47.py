# decodify/algorithms/rot47.py
def _rot47_char(c: str) -> str:
    o = ord(c)
    if 33 <= o <= 126:
        return chr(33 + ((o - 33 + 47) % 94))
    return c

def is_rot47(encoded: str) -> bool:
    """Weak cipher – detection disabled; user must specify algorithm."""
    return False
    printable = sum(1 for c in encoded if 33 <= ord(c) <= 126)
    return printable / max(len(encoded), 1) > 0.7

def decode_rot47(encoded: str) -> str:
    """
    Decode ROT47 (same as encode).
    """
    return "".join(_rot47_char(c) for c in encoded)

def encode_rot47(message: str) -> str:
    """
    Encode with ROT47.
    """
    return decode_rot47(message)
