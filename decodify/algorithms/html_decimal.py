
# decodify/algorithms/html_decimal.py

import re
import html


def is_html_decimal(encoded: str) -> bool:
    if not encoded:
        return False

    return bool(
        re.search(r"&#[0-9]+;", encoded)
    )


def decode_html_decimal(encoded: str) -> str:
    def replace(match):
        number = int(match.group(1))

        if number > 0x10FFFF or 0xD800 <= number <= 0xDFFF:
            raise ValueError("Invalid Unicode code point")

        return chr(number)

    return re.sub(r"&#([0-9]+);", replace, encoded)


def encode_html_decimal(message: str) -> str:
    return "".join(
        f"&#{ord(char)};"
        for char in message
    )
