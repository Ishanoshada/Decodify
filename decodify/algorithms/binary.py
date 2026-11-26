# decodify/algorithms/binary.py
import re

def is_binary(encoded: str) -> bool:
    """
    Check if the input is a valid binary encoded string.
    """
    binary_pattern = re.compile(r"^[01\s]+$")
    cleaned = encoded.strip()
    if not cleaned or not binary_pattern.match(cleaned):
        return False
    bits = cleaned.replace(" ", "")
    return len(bits) % 8 == 0 and len(bits) > 0

def decode_binary(encoded: str) -> str:
    """
    Decode a binary encoded string.
    """
    binary_values = encoded.replace(" ", "")
    binary_values = [binary_values[i:i+8] for i in range(0, len(binary_values), 8)]
    decoded = ""
    for binary in binary_values:
        if len(binary) == 8:
            decimal = int(binary, 2)
            decoded += chr(decimal)
    return decoded

def encode_binary(message: str) -> str:
    """
    Encode a string to binary (8-bit groups separated by spaces).
    """
    return " ".join(format(ord(c), "08b") for c in message)
