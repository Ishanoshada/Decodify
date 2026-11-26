# decodify/algorithms/quoted_printable.py
import quopri

def is_quoted_printable(encoded: str) -> bool:
    """
    Check for =XX patterns typical of quoted-printable.
    """
    import re
    return bool(re.search(r"=[0-9A-Fa-f]{2}", encoded))

def decode_quoted_printable(encoded: str) -> str:
    """
    Decode quoted-printable.
    """
    return quopri.decodestring(encoded.encode("ascii", errors="ignore")).decode("utf-8", errors="replace")

def encode_quoted_printable(message: str) -> str:
    """
    Encode to quoted-printable.
    """
    return quopri.encodestring(message.encode("utf-8")).decode("ascii")
