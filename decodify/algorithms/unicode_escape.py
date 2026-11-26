# decodify/algorithms/unicode_escape.py
import re

def is_unicode_escape(encoded: str) -> bool:
    """
    Check for \\uXXXX or \\UXXXXXXXX or \\xXX patterns.
    """
    return bool(re.search(r"\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}|\\x[0-9a-fA-F]{2}", encoded))

def decode_unicode_escape(encoded: str) -> str:
    """
    Decode Python-style unicode escapes.
    """
    try:
        return encoded.encode("utf-8").decode("unicode_escape")
    except Exception:
        # fallback manual
        def repl_u(m):
            return chr(int(m.group(1), 16))
        s = re.sub(r"\\u([0-9a-fA-F]{4})", repl_u, encoded)
        s = re.sub(r"\\U([0-9a-fA-F]{8})", repl_u, s)
        s = re.sub(r"\\x([0-9a-fA-F]{2})", repl_u, s)
        return s

def encode_unicode_escape(message: str) -> str:
    """
    Encode to \\uXXXX escapes.
    """
    return "".join(f"\\u{ord(c):04x}" for c in message)
