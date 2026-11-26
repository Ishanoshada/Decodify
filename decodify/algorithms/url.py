# decodify/algorithms/url.py
from urllib.parse import unquote, quote

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

def encode_url(message: str) -> str:
    """
    Encode a string to URL encoding (percent-encoding).
    """
    return quote(message, safe="")
