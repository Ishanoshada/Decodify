# decodify/algorithms/base36.py
_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyz"

def is_base36(encoded: str) -> bool:
    """
    Check if the input is a valid Base36 string.
    """
    cleaned = encoded.strip().lower()
    if not cleaned:
        return False
    return all(c in _ALPHABET for c in cleaned)

def decode_base36(encoded: str) -> str:
    """
    Decode a Base36 string to integer then interpret as UTF-8 bytes (big-endian).
    For text use, treat as big integer to bytes.
    """
    cleaned = encoded.strip().lower()
    num = int(cleaned, 36)
    if num == 0:
        return ""
    byte_length = (num.bit_length() + 7) // 8
    return num.to_bytes(byte_length, "big").decode("utf-8")

def encode_base36(message: str) -> str:
    """
    Encode a string to Base36 via big integer.
    """
    data = message.encode("utf-8")
    num = int.from_bytes(data, "big")
    if num == 0:
        return "0"
    result = []
    while num > 0:
        num, rem = divmod(num, 36)
        result.append(_ALPHABET[rem])
    return "".join(reversed(result))
