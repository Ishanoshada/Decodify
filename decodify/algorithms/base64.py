# decodify/algorithms/base64.py
import base64

def is_base64(encoded: str) -> bool:
    """
    Check if the input is a valid Base64 encoded string.
    """
    try:
        cleaned = encoded.strip()
        if not cleaned:
            return False
        base64.b64decode(cleaned, validate=True)
        return True
    except Exception:
        try:
            pad = 4 - (len(cleaned) % 4)
            if pad != 4:
                cleaned += "=" * pad
            base64.urlsafe_b64decode(cleaned)
            return True
        except Exception:
            return False

def decode_base64(encoded: str) -> str:
    """
    Decode a Base64 encoded string (standard or URL-safe).
    """
    cleaned = encoded.strip()
    try:
        return base64.b64decode(cleaned).decode("utf-8")
    except Exception:
        pad = 4 - (len(cleaned) % 4)
        if pad != 4:
            cleaned += "=" * pad
        return base64.urlsafe_b64decode(cleaned).decode("utf-8")

def encode_base64(message: str) -> str:
    """
    Encode a string to Base64.
    """
    return base64.b64encode(message.encode("utf-8")).decode("ascii")
