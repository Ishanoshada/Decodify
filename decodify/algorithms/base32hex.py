
# decodify/algorithms/base32hex.py

import base64
import binascii
import re


def _decode_bytes(encoded: str) -> bytes:
    cleaned = encoded.strip().upper()

    if not cleaned:
        raise ValueError("Empty Base32hex input")

    if not re.fullmatch(r"[0-9A-V]*={0,6}", cleaned):
        raise ValueError("Invalid Base32hex characters")

    unpadded = cleaned.rstrip("=")

    if len(unpadded) % 8 not in (0, 2, 4, 5, 7):
        raise ValueError("Invalid Base32hex length")

    expected_padding = (-len(unpadded)) % 8

    if "=" in cleaned and len(cleaned) - len(unpadded) != expected_padding:
        raise ValueError("Invalid Base32hex padding")

    padded = unpadded + ("=" * expected_padding)

    return base64.b32hexdecode(
        padded,
        casefold=True
    )


def is_base32hex(encoded: str) -> bool:
    try:
        if not encoded.strip():
            return False

        _decode_bytes(encoded).decode("utf-8")
        return True
    except (ValueError, UnicodeDecodeError, binascii.Error):
        return False


def decode_base32hex(encoded: str) -> str:
    return _decode_bytes(encoded).decode("utf-8")


def encode_base32hex(message: str) -> str:
    return base64.b32hexencode(
        message.encode("utf-8")
    ).decode("ascii")
