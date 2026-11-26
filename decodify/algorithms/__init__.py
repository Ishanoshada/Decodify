# decodify/algorithms/__init__.py
from .base64 import is_base64, decode_base64, encode_base64
from .hex import is_hex, decode_hex, encode_hex
from .url import is_url_encoded, decode_url, encode_url
from .binary import is_binary, decode_binary, encode_binary
from .morse import is_morse, decode_morse, encode_morse
from .base32 import is_base32, decode_base32, encode_base32
from .base58 import is_base58, decode_base58, encode_base58
from .base85 import is_base85, decode_base85, encode_base85
from .base45 import is_base45, decode_base45, encode_base45
from .base36 import is_base36, decode_base36, encode_base36
from .rot13 import is_rot13, decode_rot13, encode_rot13
from .rot47 import is_rot47, decode_rot47, encode_rot47
from .caesar import is_caesar, decode_caesar, encode_caesar, brute_force_caesar
from .atbash import is_atbash, decode_atbash, encode_atbash
from .vigenere import is_vigenere, decode_vigenere, encode_vigenere
from .rail_fence import is_rail_fence, decode_rail_fence, encode_rail_fence
from .xor_cipher import is_xor_cipher, decode_xor, encode_xor
from .baconian import is_baconian, decode_baconian, encode_baconian
from .polybius import is_polybius, decode_polybius, encode_polybius
from .affine import is_affine, decode_affine, encode_affine
from .tap_code import is_tap_code, decode_tap_code, encode_tap_code
from .nato import is_nato, decode_nato, encode_nato
from .quoted_printable import is_quoted_printable, decode_quoted_printable, encode_quoted_printable
from .html_entities import is_html_entities, decode_html_entities, encode_html_entities
from .unicode_escape import is_unicode_escape, decode_unicode_escape, encode_unicode_escape
from .uuencode import is_uuencode, decode_uuencode, encode_uuencode
from .punycode import is_punycode, decode_punycode, encode_punycode
from .jwt import is_jwt, decode_jwt, encode_jwt
from .brainfuck import is_brainfuck, decode_brainfuck, encode_brainfuck

# Registry for easy iteration
ALGORITHMS = {
    "base64": (is_base64, decode_base64, encode_base64),
    "hex": (is_hex, decode_hex, encode_hex),
    "url": (is_url_encoded, decode_url, encode_url),
    "binary": (is_binary, decode_binary, encode_binary),
    "morse": (is_morse, decode_morse, encode_morse),
    "base32": (is_base32, decode_base32, encode_base32),
    "base58": (is_base58, decode_base58, encode_base58),
    "base85": (is_base85, decode_base85, encode_base85),
    "base45": (is_base45, decode_base45, encode_base45),
    "base36": (is_base36, decode_base36, encode_base36),
    "rot13": (is_rot13, decode_rot13, encode_rot13),
    "rot47": (is_rot47, decode_rot47, encode_rot47),
    "caesar": (is_caesar, decode_caesar, encode_caesar),
    "atbash": (is_atbash, decode_atbash, encode_atbash),
    "vigenere": (is_vigenere, decode_vigenere, encode_vigenere),
    "rail_fence": (is_rail_fence, decode_rail_fence, encode_rail_fence),
    "xor": (is_xor_cipher, decode_xor, encode_xor),
    "baconian": (is_baconian, decode_baconian, encode_baconian),
    "polybius": (is_polybius, decode_polybius, encode_polybius),
    "affine": (is_affine, decode_affine, encode_affine),
    "tap_code": (is_tap_code, decode_tap_code, encode_tap_code),
    "nato": (is_nato, decode_nato, encode_nato),
    "quoted_printable": (is_quoted_printable, decode_quoted_printable, encode_quoted_printable),
    "html_entities": (is_html_entities, decode_html_entities, encode_html_entities),
    "unicode_escape": (is_unicode_escape, decode_unicode_escape, encode_unicode_escape),
    "uuencode": (is_uuencode, decode_uuencode, encode_uuencode),
    "punycode": (is_punycode, decode_punycode, encode_punycode),
    "jwt": (is_jwt, decode_jwt, encode_jwt),
    "brainfuck": (is_brainfuck, decode_brainfuck, encode_brainfuck),
}

__all__ = list(ALGORITHMS.keys()) + [
    "is_base64", "decode_base64", "encode_base64",
    "is_hex", "decode_hex", "encode_hex",
    "is_url_encoded", "decode_url", "encode_url",
    "is_binary", "decode_binary", "encode_binary",
    "is_morse", "decode_morse", "encode_morse",
    "ALGORITHMS",
]
