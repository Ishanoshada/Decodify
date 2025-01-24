# decodify/algorithms/binary.py
import re

def is_binary(encoded: str) -> bool:
    """
    Check if the input is a valid binary encoded string.
    """
    # Binary strings consist of 0s and 1s, optionally separated by spaces
    binary_pattern = re.compile(r"^[01\s]+$")
    return bool(binary_pattern.match(encoded))

def decode_binary(encoded: str) -> str:
    """
    Decode a binary encoded string.
    """
    # Remove spaces and split into 8-bit chunks
    binary_values = encoded.replace(" ", "")
    binary_values = [binary_values[i:i+8] for i in range(0, len(binary_values), 8)]
    decoded = ""
    for binary in binary_values:
        decimal = int(binary, 2)
        decoded += chr(decimal)
    return decoded