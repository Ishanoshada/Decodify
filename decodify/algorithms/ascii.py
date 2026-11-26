
# decodify/algorithms/ascii.py

def is_ascii(encoded: str) -> bool:
    try:
        if not encoded.strip():
            return False

        values = [int(value) for value in encoded.split()]

        return all(0 <= value <= 127 for value in values)

    except (ValueError, TypeError):
        return False


def decode_ascii(encoded: str) -> str:
    values = encoded.split()

    if not values:
        raise ValueError("Empty ASCII input")

    try:
        numbers = [int(value) for value in values]
    except ValueError as exc:
        raise ValueError("Invalid ASCII values") from exc

    if any(value < 0 or value > 127 for value in numbers):
        raise ValueError("ASCII values must be between 0 and 127")

    return "".join(chr(value) for value in numbers)


def encode_ascii(message: str) -> str:
    try:
        values = [str(ord(char)) for char in message]

        if any(ord(char) > 127 for char in message):
            raise ValueError("Message contains non-ASCII characters")

        return " ".join(values)

    except TypeError as exc:
        raise ValueError("Message must be a string") from exc
