# decodify/algorithms/__init__.py

# Original algorithms
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
from .quoted_printable import (
    is_quoted_printable,
    decode_quoted_printable,
    encode_quoted_printable,
)
from .html_entities import (
    is_html_entities,
    decode_html_entities,
    encode_html_entities,
)
from .unicode_escape import (
    is_unicode_escape,
    decode_unicode_escape,
    encode_unicode_escape,
)
from .uuencode import is_uuencode, decode_uuencode, encode_uuencode
from .punycode import is_punycode, decode_punycode, encode_punycode
from .jwt import is_jwt, decode_jwt, encode_jwt
from .brainfuck import is_brainfuck, decode_brainfuck, encode_brainfuck

# Additional encodings
from .ascii import is_ascii, decode_ascii, encode_ascii
from .autokey import is_autokey, decode_autokey, encode_autokey
from .base32hex import is_base32hex, decode_base32hex, encode_base32hex
from .base58_flickr import (
    is_base58_flickr,
    decode_base58_flickr,
    encode_base58_flickr,
)
from .base58_ripple import (
    is_base58_ripple,
    decode_base58_ripple,
    encode_base58_ripple,
)
from .base64url import is_base64url, decode_base64url, encode_base64url
from .base91 import is_base91, decode_base91, encode_base91
from .beaufort import is_beaufort, decode_beaufort, encode_beaufort
from .columnar_transposition import (
    is_columnar_transposition,
    decode_columnar_transposition,
    encode_columnar_transposition,
)
from .compression_bz2 import is_bz2, decode_bz2, encode_bz2
from .compression_gzip import is_gzip, decode_gzip, encode_gzip
from .compression_lzma import is_lzma, decode_lzma, encode_lzma
from .compression_zlib import is_zlib, decode_zlib, encode_zlib
from .decimal_encoding import is_decimal, decode_decimal, encode_decimal
from .deflate import is_deflate, decode_deflate, encode_deflate
from .escape import is_escape, decode_escape, encode_escape
from .gronsfeld import is_gronsfeld, decode_gronsfeld, encode_gronsfeld
from .html_decimal import (
    is_html_decimal,
    decode_html_decimal,
    encode_html_decimal,
)
from .html_hex import is_html_hex, decode_html_hex, encode_html_hex
from .hill import is_hill, decode_hill, encode_hill
from .octal import is_octal, decode_octal, encode_octal
from .playfair import is_playfair, decode_playfair, encode_playfair
from .porta import is_porta, decode_porta, encode_porta
from .rot18 import is_rot18, decode_rot18, encode_rot18
from .rot5 import is_rot5, decode_rot5, encode_rot5
from .scytale import is_scytale, decode_scytale, encode_scytale
from .substitution import (
    is_substitution,
    decode_substitution,
    encode_substitution,
)
from .unicode_codepoint import (
    is_unicode_codepoint,
    decode_unicode_codepoint,
    encode_unicode_codepoint,
)
from .utf8 import is_utf8, decode_utf8, encode_utf8
from .utf16 import is_utf16, decode_utf16, encode_utf16
from .utf32 import is_utf32, decode_utf32, encode_utf32
from .z85 import is_z85, decode_z85, encode_z85


# Registry format:
# algorithm_name: (detection_function, decode_function, encode_function)

ALGORITHMS = {
    # Original algorithms
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
    "quoted_printable": (
        is_quoted_printable,
        decode_quoted_printable,
        encode_quoted_printable,
    ),
    "html_entities": (
        is_html_entities,
        decode_html_entities,
        encode_html_entities,
    ),
    "unicode_escape": (
        is_unicode_escape,
        decode_unicode_escape,
        encode_unicode_escape,
    ),
    "uuencode": (is_uuencode, decode_uuencode, encode_uuencode),
    "punycode": (is_punycode, decode_punycode, encode_punycode),
    "jwt": (is_jwt, decode_jwt, encode_jwt),
    "brainfuck": (is_brainfuck, decode_brainfuck, encode_brainfuck),

    # Additional encodings
    "ascii": (is_ascii, decode_ascii, encode_ascii),
    "autokey": (is_autokey, decode_autokey, encode_autokey),
    "base32hex": (is_base32hex, decode_base32hex, encode_base32hex),
    "base58_flickr": (
        is_base58_flickr,
        decode_base58_flickr,
        encode_base58_flickr,
    ),
    "base58_ripple": (
        is_base58_ripple,
        decode_base58_ripple,
        encode_base58_ripple,
    ),
    "base64url": (is_base64url, decode_base64url, encode_base64url),
    "base91": (is_base91, decode_base91, encode_base91),
    "beaufort": (is_beaufort, decode_beaufort, encode_beaufort),
    "columnar_transposition": (
        is_columnar_transposition,
        decode_columnar_transposition,
        encode_columnar_transposition,
    ),
    "bz2": (is_bz2, decode_bz2, encode_bz2),
    "gzip": (is_gzip, decode_gzip, encode_gzip),
    "lzma": (is_lzma, decode_lzma, encode_lzma),
    "zlib": (is_zlib, decode_zlib, encode_zlib),
    "decimal": (is_decimal, decode_decimal, encode_decimal),
    "deflate": (is_deflate, decode_deflate, encode_deflate),
    "escape": (is_escape, decode_escape, encode_escape),
    "gronsfeld": (is_gronsfeld, decode_gronsfeld, encode_gronsfeld),
    "html_decimal": (
        is_html_decimal,
        decode_html_decimal,
        encode_html_decimal,
    ),
    "html_hex": (is_html_hex, decode_html_hex, encode_html_hex),
    "hill": (is_hill, decode_hill, encode_hill),
    "octal": (is_octal, decode_octal, encode_octal),
    "playfair": (is_playfair, decode_playfair, encode_playfair),
    "porta": (is_porta, decode_porta, encode_porta),
    "rot18": (is_rot18, decode_rot18, encode_rot18),
    "rot5": (is_rot5, decode_rot5, encode_rot5),
    "scytale": (is_scytale, decode_scytale, encode_scytale),
    "substitution": (
        is_substitution,
        decode_substitution,
        encode_substitution,
    ),
    "unicode_codepoint": (
        is_unicode_codepoint,
        decode_unicode_codepoint,
        encode_unicode_codepoint,
    ),
    "utf8": (is_utf8, decode_utf8, encode_utf8),
    "utf16": (is_utf16, decode_utf16, encode_utf16),
    "utf32": (is_utf32, decode_utf32, encode_utf32),
    "z85": (is_z85, decode_z85, encode_z85),
}


# Public exports
__all__ = [
    "ALGORITHMS",
    "brute_force_caesar",
]

for _, functions in ALGORITHMS.items():
    for function in functions:
        if function.__name__ not in __all__:
            __all__.append(function.__name__)