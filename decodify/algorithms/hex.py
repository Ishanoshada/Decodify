# decodify/algorithms/hex.py
import re

def is_hex(encoded: str) -> bool:
    """
    Check if the input is a valid Hexadecimal encoded string.
    """
    cleaned = encoded.strip().replace(" ", "").replace("0x", "").replace("0X", "")
    if len(cleaned) == 0 or len(cleaned) % 2 != 0:
        return False
    hex_pattern = re.compile(r"^[0-9a-fA-F]+$")
    if not hex_pattern.match(cleaned):
        return False
    # Prefer real hex (contains a-f) over pure 0-1 which is more likely binary
    if set(cleaned) <= set("01") and len(cleaned) >= 8:
        return False
    return True

def decode_hex(encoded: str) -> str:
    """
    Decode a Hexadecimal encoded string.
    """
    cleaned = encoded.strip().replace(" ", "").replace("0x", "").replace("0X", "")
    return bytes.fromhex(cleaned).decode("utf-8")

def encode_hex(message: str) -> str:
    """
    Encode a string to hexadecimal.
    """
    return message.encode("utf-8").hex()
