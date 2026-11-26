# decodify/algorithms/affine.py
def _modinv(a: int, m: int = 26) -> int:
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse")

def is_affine(encoded: str) -> bool:
    """Weak cipher – detection disabled; user must specify algorithm."""
    return False
    # original logic kept below for reference
    """
    Weak detection.
    """
    if not encoded.strip():
        return False
    letters = sum(1 for c in encoded if c.isalpha())
    return letters / max(len(encoded), 1) > 0.5

def decode_affine(encoded: str, a: int = 5, b: int = 8) -> str:
    """
    Decode Affine cipher (ax + b mod 26). Default a=5, b=8.
    a must be coprime with 26.
    """
    try:
        inv = _modinv(a)
    except ValueError:
        return encoded
    result = []
    for c in encoded:
        if c.isupper():
            y = ord(c) - ord('A')
            x = (inv * (y - b)) % 26
            result.append(chr(x + ord('A')))
        elif c.islower():
            y = ord(c) - ord('a')
            x = (inv * (y - b)) % 26
            result.append(chr(x + ord('a')))
        else:
            result.append(c)
    return "".join(result)

def encode_affine(message: str, a: int = 5, b: int = 8) -> str:
    """
    Encode with Affine cipher.
    """
    result = []
    for c in message:
        if c.isupper():
            x = ord(c) - ord('A')
            y = (a * x + b) % 26
            result.append(chr(y + ord('A')))
        elif c.islower():
            x = ord(c) - ord('a')
            y = (a * x + b) % 26
            result.append(chr(y + ord('a')))
        else:
            result.append(c)
    return "".join(result)
