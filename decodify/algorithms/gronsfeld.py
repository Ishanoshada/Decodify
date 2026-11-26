
# decodify/algorithms/gronsfeld.py


def _validate_key(key: str) -> str:
    if not key or not key.isascii() or not key.isdigit():
        raise ValueError("Key must contain numeric digits")
    return key


def _transform(text: str, key: str, decrypt: bool = False) -> str:
    key = _validate_key(key)
    result = []
    key_index = 0

    for char in text:
        if char.isascii() and char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = int(key[key_index % len(key)])

            if decrypt:
                shift = -shift

            result.append(
                chr((ord(char) - base + shift) % 26 + base)
            )
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def is_gronsfeld(encoded: str) -> bool:
    return bool(encoded) and encoded.isascii()


def encode_gronsfeld(message: str, key: str) -> str:
    return _transform(message, key)


def decode_gronsfeld(encoded: str, key: str) -> str:
    return _transform(encoded, key, decrypt=True)
