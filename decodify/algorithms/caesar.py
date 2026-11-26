# decodify/algorithms/caesar.py
def is_caesar(encoded: str) -> bool:
    """Weak cipher – detection disabled; user must specify algorithm."""
    return False
    # original logic kept below for reference
    """
    Weak detection for Caesar; better when algorithm forced or shift known.
    """
    if not encoded.strip():
        return False
    letters = sum(1 for c in encoded if c.isalpha())
    return letters / max(len(encoded), 1) > 0.5

def decode_caesar(encoded: str, shift: int = 3) -> str:
    """
    Decode Caesar cipher with given shift (default 3 = classic).
    """
    result = []
    for c in encoded:
        if c.isupper():
            result.append(chr((ord(c) - ord('A') - shift) % 26 + ord('A')))
        elif c.islower():
            result.append(chr((ord(c) - ord('a') - shift) % 26 + ord('a')))
        else:
            result.append(c)
    return "".join(result)

def encode_caesar(message: str, shift: int = 3) -> str:
    """
    Encode with Caesar cipher.
    """
    return decode_caesar(message, -shift)

def brute_force_caesar(encoded: str) -> dict:
    """
    Try all 25 shifts and return candidates.
    """
    return {shift: decode_caesar(encoded, shift) for shift in range(1, 26)}
