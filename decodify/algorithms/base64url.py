
# decodify/algorithms/base64url.py

import base64
import binascii
import re


def _decode_bytes(encoded: str) -> bytes:
    cleaned = encoded.strip()

    if not cleaned:
        raise ValueError("Empty Base64URL input")

    if not re.fullmatch(r"[A-Za-z0-9_-]*={0,2}", cleaned):
        raise ValueError("Invalid Base64URL characters")

    unpadded = cleaned.rstrip("=")

    if len(unpadded) % 4 == 1:
        raise ValueError("Invalid Base64URL length")

    expected_padding = (-len(unpadded)) % 4

    if "=" in cleaned and len(cleaned) - len(unpadded) != expected_padding:
        raise ValueError("Invalid Base64URL padding")

    padded = unpadded + ("=" * expected_padding)

    return base64.b64decode(
        padded,
        altchars=b"-_",
        validate=True
    )


def is_base64url(encoded: str) -> bool:
    try:
        if not encoded.strip():
            return False

        _decode_bytes(encoded).decode("utf-8")
        return True
    except (ValueError, UnicodeDecodeError, binascii.Error):
        return False


def decode_base64url(encoded: str) -> str:
    return _decode_bytes(encoded).decode("utf-8")


def encode_base64url(message: str) -> str:
    return base64.urlsafe_b64encode(
        message.encode("utf-8")
    ).decode("ascii").rstrip("=")
