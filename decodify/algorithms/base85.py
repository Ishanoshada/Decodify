# decodify/algorithms/base85.py
import base64
import re

def is_base85(encoded: str) -> bool:
    """
    Check if the input is a valid Ascii85 / Base85 string.
    Prefer strings with the Adobe <~ ~> wrappers or clear alphabet usage.
    """
    cleaned = encoded.strip()
    if not cleaned or len(cleaned) < 5:
        return False
    # strong signal: Adobe markers
    if cleaned.startswith("<~") and cleaned.endswith("~>"):
        return True
    # otherwise require the classic Ascii85 alphabet and length constraints
    # Ascii85 uses chars from ! (33) to u (117)
    if not re.match(r'^[!-u]+$', cleaned):
        return False
    # avoid colliding with base64 (which has + / = and A-Za-z0-9)
    if re.search(r'[A-Za-z0-9+/=]', cleaned) and not re.search(r'[!-u]', cleaned):
        return False
    try:
        base64.a85decode(cleaned, adobe=False)
        return True
    except Exception:
        try:
            base64.a85decode(cleaned, adobe=True)
            return True
        except Exception:
            return False

def decode_base85(encoded: str) -> str:
    """
    Decode an Ascii85 / Base85 string.
    """
    cleaned = encoded.strip()
    adobe = False
    if cleaned.startswith("<~") and cleaned.endswith("~>"):
        cleaned = cleaned[2:-2]
        adobe = True
    try:
        return base64.a85decode(cleaned, adobe=adobe).decode("utf-8")
    except Exception:
        return base64.a85decode(cleaned, adobe=not adobe).decode("utf-8")

def encode_base85(message: str) -> str:
    """
    Encode a string to Ascii85 (with <~ ~> wrappers).
    """
    return "<~" + base64.a85encode(message.encode("utf-8"), adobe=False).decode("ascii") + "~>"
