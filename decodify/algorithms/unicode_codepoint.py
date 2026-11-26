
# decodify/algorithms/unicode_codepoint.py

import re


def is_unicode_codepoint(encoded: str) -> bool:
    if not encoded.strip():
        return False

    values = encoded.split()

    try:
        for value in values:
            if not re.fullmatch(r"(?:U\+)?[0-9A-Fa-f]{1,6}", value):
                return False

            number = int(value.removeprefix("U+"), 16)

            if number > 0x10FFFF or 0xD800 <= number <= 0xDFFF:
                return False

        return True

    except ValueError:
        return False


def decode_unicode_codepoint(encoded: str) -> str:
    values = encoded.split()

    if not values:
        raise ValueError("Empty Unicode code point input")

    result = []

    for value in values:
        if not re.fullmatch(r"(?:U\+)?[0-9A-Fa-f]{1,6}", value):
            raise ValueError(f"Invalid Unicode code point: {value}")

        number = int(value.removeprefix("U+"), 16)

        if number > 0x10FFFF or 0xD800 <= number <= 0xDFFF:
            raise ValueError(f"Invalid Unicode code point: {value}")

        result.append(chr(number))

    return "".join(result)


def encode_unicode_codepoint(message: str) -> str:
    return " ".join(f"U+{ord(char):04X}" for char in message)
