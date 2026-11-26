
# decodify/algorithms/decimal_encoding.py

def is_decimal(encoded: str) -> bool:
    try:
        if not encoded.strip():
            return False

        values = encoded.split()

        return all(
            value.isdigit() and 0 <= int(value) <= 0x10FFFF
            for value in values
        )

    except (ValueError, TypeError):
        return False


def decode_decimal(encoded: str) -> str:
    values = encoded.split()

    if not values:
        raise ValueError("Empty decimal input")

    result = []

    for value in values:
        if not value.isdigit():
            raise ValueError(f"Invalid decimal value: {value}")

        number = int(value)

        if number > 0x10FFFF:
            raise ValueError(f"Invalid Unicode code point: {number}")

        if 0xD800 <= number <= 0xDFFF:
            raise ValueError(f"Surrogate code point is invalid: {number}")

        result.append(chr(number))

    return "".join(result)


def encode_decimal(message: str) -> str:
    return " ".join(str(ord(char)) for char in message)
