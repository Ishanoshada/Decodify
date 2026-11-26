
# decodify/algorithms/playfair.py

import re

ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def _create_matrix(key: str) -> str:
    if not key or not key.isascii() or not key.isalpha():
        raise ValueError("Key must contain ASCII letters")

    combined = key.upper().replace("J", "I") + ALPHABET

    return "".join(dict.fromkeys(combined))


def _prepare_text(text: str) -> list:
    cleaned = re.sub("[^A-Za-z]", "", text).upper().replace("J", "I")
    pairs = []
    index = 0

    while index < len(cleaned):
        first = cleaned[index]

        if index + 1 >= len(cleaned):
            second = "X" if first != "X" else "Q"
            index += 1
        elif cleaned[index + 1] == first:
            second = "X" if first != "X" else "Q"
            index += 1
        else:
            second = cleaned[index + 1]
            index += 2

        pairs.append((first, second))

    return pairs


def _transform(text: str, key: str, decrypt: bool = False) -> str:
    matrix = _create_matrix(key)
    result = []

    for first, second in _prepare_text(text):
        a = matrix.index(first)
        b = matrix.index(second)

        row1, col1 = divmod(a, 5)
        row2, col2 = divmod(b, 5)

        if row1 == row2:
            shift = -1 if decrypt else 1
            first = matrix[row1 * 5 + (col1 + shift) % 5]
            second = matrix[row2 * 5 + (col2 + shift) % 5]

        elif col1 == col2:
            shift = -1 if decrypt else 1
            first = matrix[((row1 + shift) % 5) * 5 + col1]
            second = matrix[((row2 + shift) % 5) * 5 + col2]

        else:
            first = matrix[row1 * 5 + col2]
            second = matrix[row2 * 5 + col1]

        result.extend([first, second])

    return "".join(result)


def is_playfair(encoded: str) -> bool:
    return bool(encoded) and encoded.isascii() and encoded.isalpha()


def encode_playfair(message: str, key: str) -> str:
    return _transform(message, key)


def decode_playfair(encoded: str, key: str) -> str:
    return _transform(encoded, key, decrypt=True)
