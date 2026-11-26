
# decodify/algorithms/z85.py

ALPHABET = (
    "0123456789abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#"
)

DECODE_TABLE = {
    char: index
    for index, char in enumerate(ALPHABET)
}


def _decode_bytes(encoded: str) -> bytes:
    cleaned = encoded.strip()

    if not cleaned:
        raise ValueError("Empty Z85 input")

    if len(cleaned) % 5 != 0:
        raise ValueError("Z85 input length must be divisible by 5")

    output = bytearray()

    for index in range(0, len(cleaned), 5):
        chunk = cleaned[index:index + 5]
        number = 0

        for char in chunk:
            if char not in DECODE_TABLE:
                raise ValueError(
                    f"Invalid Z85 character: {char!r}"
                )

            number = number * 85 + DECODE_TABLE[char]

        if number > 0xFFFFFFFF:
            raise ValueError("Invalid Z85 block value")

        output.extend(number.to_bytes(4, "big"))

    return bytes(output)


def is_z85(encoded: str) -> bool:
    try:
        if not encoded.strip():
            return False

        _decode_bytes(encoded).decode("utf-8")
        return True

    except (ValueError, UnicodeDecodeError):
        return False


def decode_z85(encoded: str) -> str:
    return _decode_bytes(encoded).decode("utf-8")


def encode_z85(message: str) -> str:
    data = message.encode("utf-8")

    if len(data) % 4 != 0:
        raise ValueError(
            "Z85 requires input bytes to be divisible by 4"
        )

    output = []

    for index in range(0, len(data), 4):
        number = int.from_bytes(
            data[index:index + 4],
            "big"
        )

        block = [""] * 5

        for position in range(4, -1, -1):
            number, remainder = divmod(number, 85)
            block[position] = ALPHABET[remainder]

        output.extend(block)

    return "".join(output)
