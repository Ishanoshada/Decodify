# decodify/algorithms/base64.py
import base64

def is_base64(encoded: str) -> bool:
    """
    Check if the input is a valid Base64 encoded string.
    """
    try:
        base64.b64decode(encoded, validate=True)
        return True
    except:
        return False

def decode_base64(encoded: str) -> str:
    """
    Decode a Base64 encoded string.
    """
    return base64.b64decode(encoded).decode("utf-8")