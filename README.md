# Decodify

**Decodify** is a Python package that automatically detects, decodes, and encodes messages using **61 encoding formats, classical ciphers, and specialized algorithms**. It provides a Python API and a command-line interface (CLI) with support for file operations and configurable cipher parameters.

---

## Features

- **61 algorithms** covering base encodings, text formats, classical ciphers, compression, and historical codes.
- **Automatic detection** with priority for distinctive encoding formats.
- **Encoding and decoding** through a unified API and CLI.
- **Keyed ciphers** with configurable keys and parameters.
- **File processing** with input and output file support.
- **Python API** for integration into other applications.
- **Algorithm listing** to explore all supported formats.
- **Probability scores** for automatic detection results.

---

## Supported Algorithms

| Category | Supported Algorithms |
|---|---|
| Base Encodings | `base32`, `base32hex`, `base36`, `base45`, `base58`, `base58_flickr`, `base58_ripple`, `base64`, `base64url`, `base85`, `base91`, `z85` |
| Text & Web Encodings | `ascii`, `decimal`, `hex`, `binary`, `octal`, `url`, `escape`, `quoted_printable`, `html_decimal`, `html_entities`, `html_hex`, `unicode_codepoint`, `unicode_escape`, `utf8`, `utf16`, `utf32`, `punycode` |
| Classical & Modern Ciphers | `affine`, `atbash`, `autokey`, `beaufort`, `caesar`, `gronsfeld`, `hill`, `playfair`, `porta`, `rail_fence`, `scytale`, `substitution`, `vigenere`, `xor`, `rot5`, `rot13`, `rot18`, `rot47` |
| Historical & Specialty Formats | `baconian`, `brainfuck`, `morse`, `nato`, `polybius`, `tap_code`, `uuencode`, `jwt` |
| Compression Formats | `bz2`, `deflate`, `gzip`, `lzma`, `zlib` |

---

## Installation

Install from PyPI:

```bash
pip install decodify
```

Or install from source:

```bash
git clone https://github.com/Ishanoshada/Decodify.git
cd Decodify
pip install -e .
```

---

## Quick Start – Python API

```python
from decodify import decode_message, encode_message, list_algorithms

# Automatically detect and decode
decoded, probabilities = decode_message("aGVsbG8=")

print(decoded)
# hello

print(probabilities)
# {'base64': 1.0}

# Decode using a specific algorithm
decoded, _ = decode_message("uryyb", algorithm="rot13")
print(decoded)
# hello

# Decode with cipher parameters
decoded, _ = decode_message(
    "ciphertext",
    algorithm="vigenere",
    key="LEMON"
)

decoded, _ = decode_message(
    "Uryyb",
    algorithm="caesar",
    shift=13
)

# Encode messages
print(encode_message("hello", "base64"))
# aGVsbG8=

print(encode_message("hello", "hex"))
# 68656c6c6f

print(encode_message("SOS", "morse"))

print(encode_message("secret", "xor", key="key"))

# List available algorithms
print(list_algorithms())
```

---

## Command-Line Interface (CLI)

### Display help

```bash
decodify --help
```

### List supported algorithms

```bash
decodify --list
```

### Automatic detection and decoding

```bash
decodify "aGVsbG8="
```

Example output:

```text
Decoded Message: hello
Algorithm Probabilities:
  base64: 1.000
```

### Decode with a specific algorithm

```bash
decodify "aGVsbG8=" --algorithm base64

decodify "68656c6c6f" --algorithm hex

decodify "uryyb" --algorithm rot13

decodify ".... . .-.. .-.. ---" --algorithm morse

decodify "01101000 01100101 01101100 01101100 01101111" --algorithm binary
```

### Encode messages

Use `-e` or `--encode` to enable encoding mode.

```bash
decodify "hello" --algorithm base64 --encode

decodify "hello" --algorithm hex --encode

decodify "hello" --algorithm binary --encode

decodify "hello" --algorithm morse --encode

decodify "hello" --algorithm rot13 --encode
```

Example output:

```text
Encoded Message: aGVsbG8=
```

### Cipher parameters

**Caesar cipher**

```bash
# Encode
decodify "hello" --algorithm caesar --encode --shift 3

# Decode
decodify "khoor" --algorithm caesar --shift 3
```

**Vigenère cipher**

```bash
# Encode
decodify "hello" --algorithm vigenere --encode --key SECRET

# Decode
decodify "ciphertext" --algorithm vigenere --key SECRET
```

**XOR cipher**

```bash
decodify "hello" --algorithm xor --encode --key secret

decodify "encoded_text" --algorithm xor --key secret
```

**Rail Fence cipher**

```bash
decodify "hello" --algorithm rail_fence --encode --rails 3

decodify "encoded_text" --algorithm rail_fence --rails 3
```

**Affine cipher**

```bash
decodify "hello" --algorithm affine --encode --a 5 --b 8

decodify "encoded_text" --algorithm affine --a 5 --b 8
```

### File operations

Read and decode a file:

```bash
decodify --file encoded.txt
```

Decode using a specific algorithm:

```bash
decodify --file encoded.txt --algorithm base64
```

Save decoded output:

```bash
decodify --file encoded.txt --algorithm base64 --output decoded.txt
```

You can also use a positional file path:

```bash
decodify encoded.txt --algorithm base64 --output decoded.txt
```

---

## CLI Options

| Option | Description |
|---|---|
| `-h`, `--help` | Display help information |
| `-f`, `--file` | Read input from a file |
| `-o`, `--output` | Save the result to a file |
| `-a`, `--algorithm` | Select a specific algorithm |
| `-e`, `--encode` | Encode instead of decode |
| `--key` | Key for keyed ciphers |
| `--shift` | Caesar cipher shift (default: 3) |
| `--rails` | Rail Fence rail count (default: 3) |
| `--a` | Affine cipher coefficient A |
| `--b` | Affine cipher coefficient B |
| `-l`, `--list` | List supported algorithms |

---

## Automatic Detection

Decodify uses heuristic detection to identify possible encoding formats.

Distinctive formats are prioritized, including:

- Base64 and other recognizable base encodings
- Morse code
- NATO phonetic alphabet
- Brainfuck
- Tap Code
- Polybius
- Baconian
- UUEncode
- JWT
- Other recognizable formats

**Note:** Automatic detection cannot reliably identify every encoding or cipher. Ambiguous classical ciphers such as ROT13, Caesar, Vigenère, XOR, Affine, and Rail Fence should be selected explicitly using `--algorithm` and the required parameters.

---

## Testing

Run the test suite:

```bash
python -m pytest tests/ -v
```

Run tests with coverage:

```bash
python -m pytest tests/ -v --cov=decodify --cov-report=term-missing
```

Current test status:

```text
64 passed
0 failed
67% code coverage
```

---

## Project Structure

```text
decodify/
├── algorithms/
│   ├── __init__.py
│   ├── base64.py
│   ├── base32.py
│   ├── morse.py
│   ├── caesar.py
│   ├── ...
├── __init__.py
├── cli.py
└── decodify.py

tests/
└── test_decodify.py

setup.py
README.md
```

---

## Contributing

Contributions are welcome!

To add a new algorithm:

1. Create a module under `decodify/algorithms/`.
2. Implement the detection, decoding, and encoding functions where applicable.
3. Register the algorithm in `decodify/algorithms/__init__.py`.
4. Add tests under `tests/`.
5. Submit a pull request.

---

## License

MIT License

## Author

**Ishan Oshada**

- GitHub: https://github.com/Ishanoshada
- Repository: https://github.com/Ishanoshada/Decodify

---

**Decodify – Detect, Decode, and Encode.** 🚀