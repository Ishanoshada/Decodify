# decodify/algorithms/__init__.py
from .base64 import is_base64, decode_base64
from .hex import is_hex, decode_hex
from .url import is_url_encoded, decode_url
from .binary import is_binary, decode_binary
from .morse import is_morse, decode_morse