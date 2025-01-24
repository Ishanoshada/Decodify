# decodify/algorithms/hex.py
import re

def is_hex(encoded: str) -> bool:
    """
    Check if the input is a valid Hexadecimal encoded string.
    """
    hex_pattern = re.compile(r"^[0-9a-fA-F]+$")
    return bool(hex_pattern.match(encoded))

def decode_hex(encoded: str) -> str:
    """
    Decode a Hexadecimal encoded string.
    """
    return bytes.fromhex(encoded).decode("utf-8")