# decodify/algorithms/base32.py
import base64
import re

def is_base32(encoded: str) -> bool:
    """
    Check if the input is a valid Base32 encoded string.
    """
    cleaned = encoded.strip().upper().replace(" ", "")
    if not cleaned or len(cleaned) % 8 not in (0, 2, 4, 5, 7):  # with padding
        # allow without strict padding check
        pass
    pattern = re.compile(r"^[A-Z2-7=]+$")
    if not pattern.match(cleaned):
        return False
    try:
        base64.b32decode(cleaned, casefold=True)
        return True
    except Exception:
        return False

def decode_base32(encoded: str) -> str:
    """
    Decode a Base32 encoded string.
    """
    cleaned = encoded.strip().upper().replace(" ", "")
    # fix padding
    pad = 8 - (len(cleaned) % 8)
    if pad != 8:
        cleaned += "=" * pad
    return base64.b32decode(cleaned).decode("utf-8")

def encode_base32(message: str) -> str:
    """
    Encode a string to Base32.
    """
    return base64.b32encode(message.encode("utf-8")).decode("ascii")
