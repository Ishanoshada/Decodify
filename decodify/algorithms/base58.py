# decodify/algorithms/base58.py
_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
_BASE = len(_ALPHABET)

def is_base58(encoded: str) -> bool:
    """
    Check if the input looks like Base58 (Bitcoin-style).
    """
    cleaned = encoded.strip()
    if not cleaned or len(cleaned) < 4:
        return False
    if not all(c in _ALPHABET for c in cleaned):
        return False
    # Prefer strings that contain both upper and lower (typical of base58)
    has_upper = any(c.isupper() for c in cleaned)
    has_lower = any(c.islower() for c in cleaned)
    has_digit = any(c.isdigit() for c in cleaned)
    return (has_upper and has_lower) or (has_digit and (has_upper or has_lower))

def decode_base58(encoded: str) -> str:
    """
    Decode a Base58 string to UTF-8 text.
    """
    cleaned = encoded.strip()
    num = 0
    for c in cleaned:
        num = num * _BASE + _ALPHABET.index(c)
    if num == 0:
        return ""
    byte_length = (num.bit_length() + 7) // 8
    result = num.to_bytes(byte_length, "big")
    leading = 0
    for c in cleaned:
        if c == "1":
            leading += 1
        else:
            break
    return (b"\x00" * leading + result).decode("utf-8")

def encode_base58(message: str) -> str:
    """
    Encode a string to Base58.
    """
    data = message.encode("utf-8")
    num = int.from_bytes(data, "big")
    if num == 0:
        return "1" * len(data)
    result = []
    while num > 0:
        num, rem = divmod(num, _BASE)
        result.append(_ALPHABET[rem])
    leading = 0
    for b in data:
        if b == 0:
            leading += 1
        else:
            break
    return "1" * leading + "".join(reversed(result))
