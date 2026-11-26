# decodify/algorithms/atbash.py
def _atbash_char(c: str) -> str:
    if c.isupper():
        return chr(ord('Z') - (ord(c) - ord('A')))
    if c.islower():
        return chr(ord('z') - (ord(c) - ord('a')))
    return c

def is_atbash(encoded: str) -> bool:
    """Weak cipher – detection disabled; user must specify algorithm."""
    return False
    # original logic kept below for reference
    """
    Weak detection based on letter density.
    """
    if not encoded.strip():
        return False
    letters = sum(1 for c in encoded if c.isalpha())
    return letters / max(len(encoded), 1) > 0.5

def decode_atbash(encoded: str) -> str:
    """
    Decode Atbash (same as encode).
    """
    return "".join(_atbash_char(c) for c in encoded)

def encode_atbash(message: str) -> str:
    """
    Encode with Atbash.
    """
    return decode_atbash(message)
