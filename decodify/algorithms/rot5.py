
# decodify/algorithms/rot5.py

def _transform(text: str) -> str:
    result = []

    for char in text:
        if char.isdigit() and char.isascii():
            result.append(str((int(char) + 5) % 10))
        else:
            result.append(char)

    return "".join(result)


def is_rot5(encoded: str) -> bool:
    return bool(encoded) and any(
        char.isdigit() and char.isascii()
        for char in encoded
    )


def decode_rot5(encoded: str) -> str:
    return _transform(encoded)


def encode_rot5(message: str) -> str:
    return _transform(message)
