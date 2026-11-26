
# decodify/algorithms/scytale.py

def _validate_key(key: int) -> int:
    if type(key) is not int or key <= 0:
        raise ValueError("Key must be a positive integer")
    return key


def is_scytale(encoded: str) -> bool:
    return bool(encoded)


def encode_scytale(message: str, key: int) -> str:
    key = _validate_key(key)

    return "".join(
        message[column::key]
        for column in range(key)
    )


def decode_scytale(encoded: str, key: int) -> str:
    key = _validate_key(key)

    if not encoded:
        return ""

    rows = (len(encoded) + key - 1) // key
    extra = len(encoded) % key

    if extra == 0:
        extra = key

    columns = []
    position = 0

    for column in range(key):
        length = rows if column < extra else rows - 1
        columns.append(encoded[position:position + length])
        position += length

    result = []

    for row in range(rows):
        for column in range(key):
            if row < len(columns[column]):
                result.append(columns[column][row])

    return "".join(result)
