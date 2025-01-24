# decodify/algorithms/url.py
from urllib.parse import unquote

def is_url_encoded(encoded: str) -> bool:
    """
    Check if the input is a valid URL encoded string.
    """
    return "%" in encoded

def decode_url(encoded: str) -> str:
    """
    Decode a URL encoded string.
    """
    return unquote(encoded)