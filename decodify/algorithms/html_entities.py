# decodify/algorithms/html_entities.py
import html
import re

def is_html_entities(encoded: str) -> bool:
    """
    Check for &...; patterns.
    """
    return bool(re.search(r"&[#a-zA-Z0-9]+;", encoded))

def decode_html_entities(encoded: str) -> str:
    """
    Decode HTML entities.
    """
    return html.unescape(encoded)

def encode_html_entities(message: str) -> str:
    """
    Encode to HTML entities (named where possible).
    """
    return html.escape(message)
