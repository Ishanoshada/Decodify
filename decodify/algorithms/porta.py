
# decodify/algorithms/porta.py

def _transform(text: str, key: str) -> str:
    if not key or not key.isascii() or not key.isalpha():
        raise ValueError("Key must contain ASCII letters")

    result = []
    key_index = 0
    key = key.upper()

    for char in text:
        if char.isascii() and char.isalpha():
            key_value = ord(key[key_index % len(key)]) - ord("A")
            shift = key_value // 2

            value = ord(char.upper()) - ord("A")

            if value < 13:
                transformed = 13 + ((value + shift) % 13)
            else:
                transformed = (value - 13 - shift) % 13

            output = chr(ord("A") + transformed)

            result.append(
                output if char.isupper() else output.lower()
            )

            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def is_porta(encoded: str) -> bool:
    return bool(encoded) and encoded.isascii()


def encode_porta(message: str, key: str) -> str:
    return _transform(message, key)


def decode_porta(encoded: str, key: str) -> str:
    return _transform(encoded, key)
