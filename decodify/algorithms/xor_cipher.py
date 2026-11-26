# decodify/algorithms/xor_cipher.py
def is_xor_cipher(encoded: str) -> bool:
    """Weak cipher – detection disabled; user must specify algorithm."""
    return False
    # original logic kept below for reference
    """
    Detection is not reliable without key; treat as possible if printable after common keys.
    """
    return bool(encoded.strip())

def decode_xor(encoded: str, key: str = "key") -> str:
    """
    Decode XOR cipher with repeating key. Input assumed to be the ciphertext string.
    """
    if not key:
        key = "\x00"
    result = []
    for i, c in enumerate(encoded):
        result.append(chr(ord(c) ^ ord(key[i % len(key)])))
    return "".join(result)

def encode_xor(message: str, key: str = "key") -> str:
    """
    Encode with XOR cipher (same operation).
    """
    return decode_xor(message, key)
