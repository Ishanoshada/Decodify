
# decodify/algorithms/base58_ripple.py

ALPHABET = "rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz"
DECODE_TABLE = {char: index for index, char in enumerate(ALPHABET)}


def _decode_bytes(encoded: str) -> bytes:
    encoded = encoded.strip()

    if not encoded:
        raise ValueError("Empty Ripple Base58 input")

    number = 0

    for char in encoded:
        if char not in DECODE_TABLE:
            raise ValueError(f"Invalid Ripple Base58 character: {char!r}")
        number = number * 58 + DECODE_TABLE[char]

    zeros = len(encoded) - len(encoded.lstrip(ALPHABET[0]))
    decoded = number.to_bytes((number.bit_length() + 7) // 8, "big") if number else b""

    return b"\x00" * zeros + decoded


def is_base58_ripple(encoded: str) -> bool:
    try:
        _decode_bytes(encoded).decode("utf-8")
        return bool(encoded.strip())
    except (ValueError, UnicodeDecodeError):
        return False


def decode_base58_ripple(encoded: str) -> str:
    return _decode_bytes(encoded).decode("utf-8")


def encode_base58_ripple(message: str) -> str:
    data = message.encode("utf-8")

    if not data:
        return ""

    zeros = len(data) - len(data.lstrip(b"\x00"))
    number = int.from_bytes(data, "big")
    result = []

    while number:
        number, remainder = divmod(number, 58)
        result.append(ALPHABET[remainder])

    return ALPHABET[0] * zeros + "".join(reversed(result))
