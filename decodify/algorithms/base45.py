# decodify/algorithms/base45.py
# RFC 9285 Base45
_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
_BASE = 45

def is_base45(encoded: str) -> bool:
    """
    Check if the input is valid Base45.
    Require presence of characteristic chars that distinguish from hex/base64.
    """
    cleaned = encoded.strip()
    if not cleaned or len(cleaned) < 2 or len(cleaned) % 3 == 1:
        return False
    if not all(c in _ALPHABET for c in cleaned):
        return False
    # Base45 often contains space, $, %, *, +, -, ., / or digits mixed with upper
    # Avoid pure hex or pure digits which are more likely hex/base36
    special = set(" $%*+-./:")
    if not any(c in special for c in cleaned) and cleaned.isalnum() and all(c in "0123456789ABCDEFabcdef" for c in cleaned):
        return False  # looks like hex
    # Exclude pure Morse-like (mostly . -)
    if set(cleaned) <= set(". -/") and cleaned.count(".") + cleaned.count("-") > len(cleaned) * 0.5:
        return False
    return True

def decode_base45(encoded: str) -> str:
    """
    Decode a Base45 string (RFC 9285).
    """
    cleaned = encoded.strip()
    result = bytearray()
    i = 0
    while i < len(cleaned):
        if i + 2 < len(cleaned):
            a = _ALPHABET.index(cleaned[i])
            b = _ALPHABET.index(cleaned[i+1])
            c = _ALPHABET.index(cleaned[i+2])
            n = a + b * 45 + c * 45 * 45
            result.append(n // 256)
            result.append(n % 256)
            i += 3
        else:
            a = _ALPHABET.index(cleaned[i])
            b = _ALPHABET.index(cleaned[i+1])
            n = a + b * 45
            result.append(n)
            i += 2
    return bytes(result).decode("utf-8")

def encode_base45(message: str) -> str:
    """
    Encode a string to Base45 (RFC 9285).
    """
    data = message.encode("utf-8")
    result = []
    i = 0
    while i < len(data):
        if i + 1 < len(data):
            n = data[i] * 256 + data[i+1]
            c = n // (45 * 45)
            n %= (45 * 45)
            b = n // 45
            a = n % 45
            result.append(_ALPHABET[a])
            result.append(_ALPHABET[b])
            result.append(_ALPHABET[c])
            i += 2
        else:
            n = data[i]
            b = n // 45
            a = n % 45
            result.append(_ALPHABET[a])
            result.append(_ALPHABET[b])
            i += 1
    return "".join(result)
