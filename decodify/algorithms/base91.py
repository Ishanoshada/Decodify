
# decodify/algorithms/base91.py

ALPHABET = (
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    '0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~"'
)

DECODE_TABLE = {char: index for index, char in enumerate(ALPHABET)}


def _decode_bytes(encoded: str) -> bytes:
    cleaned = encoded.strip()

    if not cleaned:
        raise ValueError("Empty Base91 input")

    output = bytearray()
    buffer = 0
    bits = 0
    value = -1

    for char in cleaned:
        if char not in DECODE_TABLE:
            raise ValueError(f"Invalid Base91 character: {char!r}")

        digit = DECODE_TABLE[char]

        if value < 0:
            value = digit
        else:
            value += digit * 91
            buffer |= value << bits

            if (value & 8191) > 88:
                bits += 13
            else:
                bits += 14

            while bits >= 8:
                output.append(buffer & 255)
                buffer >>= 8
                bits -= 8

            value = -1

    if value >= 0:
        buffer |= value << bits
        bits += 7

        while bits >= 8:
            output.append(buffer & 255)
            buffer >>= 8
            bits -= 8

    return bytes(output)


def is_base91(encoded: str) -> bool:
    try:
        if not encoded.strip():
            return False

        _decode_bytes(encoded).decode("utf-8")
        return True
    except (ValueError, UnicodeDecodeError):
        return False


def decode_base91(encoded: str) -> str:
    return _decode_bytes(encoded).decode("utf-8")


def encode_base91(message: str) -> str:
    data = message.encode("utf-8")

    output = []
    buffer = 0
    bits = 0

    for byte in data:
        buffer |= byte << bits
        bits += 8

        if bits > 13:
            value = buffer & 8191

            if value > 88:
                buffer >>= 13
                bits -= 13
            else:
                value = buffer & 16383
                buffer >>= 14
                bits -= 14

            output.append(ALPHABET[value % 91])
            output.append(ALPHABET[value // 91])

    if bits:
        output.append(ALPHABET[buffer % 91])

        if bits > 7 or buffer > 90:
            output.append(ALPHABET[buffer // 91])

    return "".join(output)
