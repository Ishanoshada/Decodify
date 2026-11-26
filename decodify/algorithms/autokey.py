
# decodify/algorithms/autokey.py


def _validate_key(key: str) -> str:
    if not key or not key.isascii() or not key.isalpha():
        raise ValueError("Key must contain ASCII letters")
    return key.upper()


def encode_autokey(message: str, key: str) -> str:
    key = _validate_key(key)
    key_stream = list(key)
    result = []
    index = 0

    for char in message:
        if char.isascii() and char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            plain = ord(char.upper()) - 65
            shift = ord(key_stream[index]) - 65

            result.append(chr(base + (plain + shift) % 26))
            key_stream.append(chr(65 + plain))
            index += 1
        else:
            result.append(char)

    return "".join(result)


def decode_autokey(encoded: str, key: str) -> str:
    key = _validate_key(key)
    key_stream = list(key)
    result = []
    index = 0

    for char in encoded:
        if char.isascii() and char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            cipher = ord(char.upper()) - 65
            shift = ord(key_stream[index]) - 65

            plain = (cipher - shift) % 26
            result.append(chr(base + plain))
            key_stream.append(chr(65 + plain))
            index += 1
        else:
            result.append(char)

    return "".join(result)


def is_autokey(encoded: str) -> bool:
    return bool(encoded) and encoded.isascii()
