
# decodify/algorithms/hill.py

import math
import re


def _validate_key(key):
    if (
        not isinstance(key, (list, tuple))
        or len(key) != 2
        or any(not isinstance(row, (list, tuple)) or len(row) != 2 for row in key)
    ):
        raise ValueError("Key must be a 2x2 matrix")

    if any(type(value) is not int for row in key for value in row):
        raise ValueError("Matrix values must be integers")

    a, b = key[0]
    c, d = key[1]

    determinant = (a * d - b * c) % 26

    if math.gcd(determinant, 26) != 1:
        raise ValueError("Key matrix is not invertible modulo 26")

    return [[value % 26 for value in row] for row in key]


def _inverse_key(key):
    a, b = key[0]
    c, d = key[1]

    determinant = (a * d - b * c) % 26
    inverse_det = pow(determinant, -1, 26)

    return [
        [(d * inverse_det) % 26, (-b * inverse_det) % 26],
        [(-c * inverse_det) % 26, (a * inverse_det) % 26],
    ]


def _transform_letters(text, key):
    letters = [char.upper() for char in text if char.isascii() and char.isalpha()]

    if len(letters) % 2:
        letters.append("X")

    output = []
    a, b = key[0]
    c, d = key[1]

    for i in range(0, len(letters), 2):
        x = ord(letters[i]) - 65
        y = ord(letters[i + 1]) - 65

        first = (a * x + b * y) % 26
        second = (c * x + d * y) % 26

        output.extend([chr(first + 65), chr(second + 65)])

    return "".join(output)


def is_hill(encoded: str) -> bool:
    return bool(encoded) and encoded.isascii() and encoded.isalpha()


def encode_hill(message: str, key) -> str:
    matrix = _validate_key(key)
    return _transform_letters(message, matrix)


def decode_hill(encoded: str, key) -> str:
    matrix = _validate_key(key)
    inverse = _inverse_key(matrix)

    decoded = _transform_letters(encoded, inverse)

    return decoded[:-1] if decoded.endswith("X") else decoded
