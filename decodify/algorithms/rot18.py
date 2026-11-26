
# decodify/algorithms/rot18.py

def _transform(text: str) -> str:
    result = []

    for char in text:
        if "a" <= char <= "z":
            result.append(chr((ord(char) - 97 + 13) % 26 + 97))
        elif "A" <= char <= "Z":
            result.append(chr((ord(char) - 65 + 13) % 26 + 65))
        elif "0" <= char <= "9":
            result.append(str((int(char) + 5) % 10))
        else:
            result.append(char)

    return "".join(result)


def is_rot18(encoded: str) -> bool:
    return bool(encoded) and any(
        char.isalnum() and char.isascii()
        for char in encoded
    )


def decode_rot18(encoded: str) -> str:
    return _transform(encoded)


def encode_rot18(message: str) -> str:
    return _transform(message)
