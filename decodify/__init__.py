# decodify/__init__.py
from .decodify import Decodify

# Expose the functions directly
detect_algorithm = Decodify.detect_algorithm
decode_message = Decodify.decode_message