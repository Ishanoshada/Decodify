# decodify/algorithms/punycode.py
def is_punycode(encoded: str) -> bool:
    """
    Check for xn-- prefix (IDNA / Punycode domain labels).
    """
    return "xn--" in encoded.lower()

def decode_punycode(encoded: str) -> str:
    """
    Decode Punycode / IDNA domain to Unicode.
    """
    try:
        return encoded.encode("ascii").decode("idna")
    except Exception:
        # try pure punycode on label
        try:
            import encodings.idna
            return encodings.idna.ToUnicode(encoded)
        except Exception as e:
            return f"Error: {e}"

def encode_punycode(message: str) -> str:
    """
    Encode Unicode domain to Punycode / IDNA.
    """
    try:
        return message.encode("idna").decode("ascii")
    except Exception as e:
        return f"Error: {e}"
