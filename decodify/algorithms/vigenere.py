# decodify/algorithms/vigenere.py
def is_vigenere(encoded: str) -> bool:
    """Weak cipher – detection disabled; user must specify algorithm."""
    return False
    # original logic kept below for reference
    """
    Weak detection; Vigenère needs a key.
    """
    if not encoded.strip():
        return False
    letters = sum(1 for c in encoded if c.isalpha())
    return letters / max(len(encoded), 1) > 0.5

def decode_vigenere(encoded: str, key: str = "KEY") -> str:
    """
    Decode Vigenère with the given key.
    """
    key = key.upper()
    result = []
    key_idx = 0
    for c in encoded:
        if c.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord('A')
            if c.isupper():
                result.append(chr((ord(c) - ord('A') - shift) % 26 + ord('A')))
            else:
                result.append(chr((ord(c) - ord('a') - shift) % 26 + ord('a')))
            key_idx += 1
        else:
            result.append(c)
    return "".join(result)

def encode_vigenere(message: str, key: str = "KEY") -> str:
    """
    Encode with Vigenère cipher.
    """
    key = key.upper()
    result = []
    key_idx = 0
    for c in message:
        if c.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord('A')
            if c.isupper():
                result.append(chr((ord(c) - ord('A') + shift) % 26 + ord('A')))
            else:
                result.append(chr((ord(c) - ord('a') + shift) % 26 + ord('a')))
            key_idx += 1
        else:
            result.append(c)
    return "".join(result)
