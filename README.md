# Decodify

**Decodify** is a Python package that detects and decodes (or encodes) messages using **29 classic and modern** encodings and ciphers. It provides both a simple Python API and a command-line interface.

---

## Features

- **29 algorithms** covering base encodings, web/text encodings, classical ciphers, and historical specialty codes
- **Automatic detection** with priority for distinctive formats
- **Encode + decode** round-trip support for every algorithm
- **Keyed ciphers** (Caesar, Vigenère, XOR, Affine, Rail Fence) accept keys/shifts via API or CLI
- **CLI** with file I/O, algorithm forcing, and encoding mode

---

## Supported Algorithms

| Category | Algorithms |
|----------|------------|
| **Base encodings** | `base64`, `base32`, `base58`, `base85` (Ascii85), `base45` (RFC 9285), `base36`, `hex`, `binary` |
| **Text / web** | `url`, `quoted_printable`, `html_entities`, `unicode_escape`, `punycode`, `jwt` (header+payload) |
| **Classical ciphers** | `rot13`, `rot47`, `caesar`, `atbash`, `vigenere`, `rail_fence`, `affine`, `xor` |
| **Historical / specialty** | `morse`, `baconian`, `polybius`, `tap_code`, `nato`, `uuencode`, `brainfuck` |

---

## Installation

```bash
pip install -e .
# or
pip install decodify
```

---

## Quick Start (Python)

```python
from decodify import decode_message, encode_message, list_algorithms

# Auto-detect + decode
text, probs = decode_message("SGVsbG8=")
print(text)          # Hello
print(probs)         # {'base64': 1.0, ...}

# Force algorithm
text, _ = decode_message("Uryyb", algorithm="rot13")
text, _ = decode_message("...", algorithm="vigenere", key="LEMON")
text, _ = decode_message("...", algorithm="caesar", shift=13)

# Encode
print(encode_message("Hello World", "base64"))
print(encode_message("SOS", "nato"))
print(encode_message("Attack at dawn", "caesar", shift=4))
print(encode_message("secret", "xor", key="key"))

print(list_algorithms())
```

---

## CLI

```bash
# Auto-detect
decodify "SGVsbG8="

# Force algorithm
decodify -a base64 "SGVsbG8="
decodify -a morse ".... . .-.. .-.. ---"
decodify -a caesar --shift 13 "Uryyb"
decodify -a vigenere --key SECRET "ciphertext"

# Encode
decodify -e -a base64 "Hello World"
decodify -e -a nato "HELP"

# Files
decodify -f encoded.txt -o decoded.txt

# List all algorithms
decodify --list
```

---

## Notes on detection

Detection is heuristic. Distinctive formats (JWT, uuencode, Brainfuck, Tap code, Morse, NATO, Baconian, Polybius, Base45/58/85, etc.) are preferred. Ambiguous classical ciphers (Caesar, Vigenère, ROT, XOR, Affine, Rail Fence) are **not** auto-detected — pass `-a` / `algorithm=` explicitly together with the key/shift when needed.

---

## License

MIT

## Contributing

Contributions welcome — add new algorithms under `decodify/algorithms/` following the `is_X` / `decode_X` / `encode_X` pattern and register them in `algorithms/__init__.py`.

## Contact / Original author

- GitHub: [ishanoshada](https://github.com/ishanoshada)
- Repository: https://github.com/ishanoshada/decodify

Enjoy decoding with **Decodify**! 🚀
