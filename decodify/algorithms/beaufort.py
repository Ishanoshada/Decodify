
# decodify/algorithms/beaufort.py


def _transform(text: str, key: str) -> str:
    if not key or not key.isascii() or not key.isalpha():
        raise ValueError("Key must contain ASCII letters")

    key = key.upper()
    result = []
    key_index = 0

    for char in text:
        if char.isascii() and char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            value = ord(char.upper()) - 65
            shift = ord(key[key_index % len(key)]) - 65

            result.append(chr(base + (shift - value) % 26))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def is_beaufort(encoded: str) -> bool:
    return bool(encoded) and encoded.isascii()


def decode_beaufort(encoded: str, key: str) -> str:
    return _transform(encoded, key)


def encode_beaufort(message: str, key: str) -> str:
    return _transform(message, key)
