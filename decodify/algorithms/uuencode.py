# decodify/algorithms/uuencode.py
import binascii
import re

def is_uuencode(encoded: str) -> bool:
    """
    Check for classic uuencode header or begin line.
    """
    return "begin " in encoded.lower() or bool(re.match(r"^begin\s+\d+", encoded, re.I | re.M))

def decode_uuencode(encoded: str) -> str:
    """
    Decode uuencoded data.
    """
    try:
        # extract payload between begin and end
        lines = encoded.strip().splitlines()
        payload = []
        in_data = False
        for line in lines:
            if line.lower().startswith("begin "):
                in_data = True
                continue
            if line.strip().lower() == "end":
                break
            if in_data:
                payload.append(line)
        data = "\n".join(payload)
        return binascii.a2b_uu(data).decode("utf-8", errors="replace")
    except Exception as e:
        # try whole string
        try:
            return binascii.a2b_uu(encoded).decode("utf-8", errors="replace")
        except Exception:
            return f"Error decoding uuencode: {e}"

def encode_uuencode(message: str, filename: str = "file") -> str:
    """
    Encode to uuencode format.
    """
    data = message.encode("utf-8")
    encoded = binascii.b2a_uu(data).decode("ascii")
    return f"begin 644 {filename}\n{encoded}end\n"
