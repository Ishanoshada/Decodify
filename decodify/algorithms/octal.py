
# decodify/algorithms/octal.py

def is_octal(encoded: str) -> bool:
    if not encoded.strip():
        return False

    try:
        values = encoded.split()
        return all(
            value.isdigit() and all(char in "01234567" for char in value)
            and int(value, 8) <= 0x10FFFF
            and not 0xD800 <= int(value, 8) <= 0xDFFF
            for value in values
        )
    except ValueError:
        return False


def decode_octal(encoded: str) -> str:
    values = encoded.split()

    if not values:
        raise ValueError("Empty octal input")

    result = []

    for value in values:
        if not value or any(char not in "01234567" for char in value):
            raise ValueError(f"Invalid octal value: {value}")

        number = int(value, 8)

        if number > 0x10FFFF or 0xD800 <= number <= 0xDFFF:
            raise ValueError(f"Invalid Unicode code point: {value}")

        result.append(chr(number))

    return "".join(result)


def encode_octal(message: str) -> str:
    return " ".join(format(ord(char), "o") for char in message)
