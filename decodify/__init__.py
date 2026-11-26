# decodify/__init__.py
from .decodify import Decodify

# Expose the main class and convenience functions
detect_algorithm = Decodify.detect_algorithm
decode_message = Decodify.decode_message
encode_message = Decodify.encode_message
list_algorithms = Decodify.list_algorithms

__version__ = "0.1.4"
__all__ = [
    "Decodify",
    "detect_algorithm",
    "decode_message",
    "encode_message",
    "list_algorithms",
]
