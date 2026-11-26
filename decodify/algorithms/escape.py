
# decodify/algorithms/escape.py

import codecs


def is_escape(encoded: str) -> bool:
    if not encoded:
        return False

    try:
        codecs.decode(encoded.encode("ascii"), "unicode_escape")
        return "\\" in encoded
    except (UnicodeEncodeError, UnicodeDecodeError, ValueError):
        return False


def decode_escape(encoded: str) -> str:
    try:
        return codecs.decode(encoded.encode("ascii"), "unicode_escape")
    except (UnicodeEncodeError, UnicodeDecodeError, ValueError) as exc:
        raise ValueError("Invalid escape sequence") from exc


def encode_escape(message: str) -> str:
    return message.encode("unicode_escape").decode("ascii")
