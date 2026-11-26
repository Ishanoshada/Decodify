
# decodify/algorithms/columnar_transposition.py

def _validate_key(key: str) -> str:
    if not key or not key.isascii() or not key.isalpha():
        raise ValueError("Key must contain ASCII letters only")
    return key.upper()


def _column_order(key: str) -> list:
    return sorted(range(len(key)), key=lambda i: (key[i], i))


def is_columnar_transposition(encoded: str) -> bool:
    return bool(encoded) and encoded.isascii()


def encode_columnar_transposition(message: str, key: str) -> str:
    key = _validate_key(key)
    columns = len(key)

    order = _column_order(key)

    return "".join(
        message[column::columns]
        for column in order
    )


def decode_columnar_transposition(encoded: str, key: str) -> str:
    key = _validate_key(key)

    if not encoded:
        return ""

    columns = len(key)
    rows = (len(encoded) + columns - 1) // columns
    extra = len(encoded) % columns

    if extra == 0:
        extra = columns

    column_data = {}
    position = 0

    for column in _column_order(key):
        length = rows if column < extra else rows - 1

        column_data[column] = encoded[position:position + length]
        position += length

    result = []

    for row in range(rows):
        for column in range(columns):
            if row < len(column_data[column]):
                result.append(column_data[column][row])

    return "".join(result)
