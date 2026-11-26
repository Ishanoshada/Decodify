
# decodify/algorithms/html_hex.py

import re


def is_html_hex(encoded: str) -> bool:
    if not encoded:
        return False

    return bool(
        re.search(r"&#[xX][0-9a-fA-F]+;", encoded)
    )


def decode_html_hex(encoded: str) -> str:
    def replace(match):
        number = int(match.group(1), 16)

        if number > 0x10FFFF or 0xD800 <= number <= 0xDFFF:
            raise ValueError("Invalid Unicode code point")

        return chr(number)

    return re.sub(
        r"&#[xX]([0-9a-fA-F]+);",
        replace,
        encoded
    )


def encode_html_hex(message: str) -> str:
    return "".join(
        f"&#x{ord(char):X};"
        for char in message
    )
