
# decodify/algorithms/substitution.py

import string

ALPHABET = string.ascii_uppercase


def _validate_key(key: str) -> str:
    if (
        not isinstance(key, str)
        or len(key) != 26
        or not key.isascii()
        or not key.isalpha()
        or len(set(key.upper())) != 26
    ):
        raise ValueError("Key must contain 26 unique ASCII letters")

    return key.upper()


def is_substitution(encoded: str) -> bool:
    return bool(encoded) and encoded.isascii()


def encode_substitution(message: str, key: str) -> str:
    key = _validate_key(key)
    table = str.maketrans(
        ALPHABET + ALPHABET.lower(),
        key + key.lower()
    )
    return message.translate(table)


def decode_substitution(encoded: str, key: str) -> str:
    key = _validate_key(key)
    table = str.maketrans(
        key + key.lower(),
        ALPHABET + ALPHABET.lower()
    )
    return encoded.translate(table)
