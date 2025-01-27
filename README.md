# Decodify

**Decodify** is a Python package designed to detect and decode messages encoded with various algorithms. It supports multiple encoding schemes and provides a simple interface for decoding messages directly or from files.

---

## Features

- **Multiple Encoding Algorithms**: Supports Base64, Hexadecimal, URL Encoding, Binary, and Morse Code.
- **Automatic Detection**: Detects the encoding algorithm used in a message.
- **Command-Line Interface (CLI)**: Decode messages directly from the terminal or from files.
- **File Support**: Decode messages stored in files and save the output to a file.

---

## Installation

You can install `decodify` using `pip`:

```bash
pip install decodify
```

---

## Usage

### Python API

You can use the `decodify` package in your Python code to decode messages.

```python
from decodify import decode_message

# Decode a Base64 encoded message
encoded_message = "aGVsbG8="
decoded, probabilities = decode_message(encoded_message)

print(f"Decoded Message: {decoded}")
print(f"Algorithm Probabilities: {probabilities}")
```

### Command-Line Interface (CLI)

You can use the `decodify` CLI to decode messages directly from the terminal.

#### Decode a Message

```bash
decodify "aGVsbG8="
```

#### Decode a Message from a File

```bash
decodify encoded.txt -f
```

#### Specify an Algorithm

```bash
decodify "aGVsbG8=" --algorithm base64
```

#### Save the Decoded Message to a File

```bash
decodify "aGVsbG8=" --output decoded.txt
```

---

## Supported Algorithms

| Algorithm     | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **Base64**    | Decodes Base64 encoded strings.                                             |
| **Hexadecimal** | Decodes hexadecimal encoded strings.                                       |
| **URL Encoding** | Decodes URL-encoded strings (e.g., `hello%20world` → `hello world`).       |
| **Binary**    | Decodes binary encoded strings (e.g., `01101000 01100101` → `he`).          |
| **Morse Code** | Decodes Morse code strings (e.g., `.... . .-.. .-.. ---` → `HELLO`).       |

---

## Examples

### Decoding a Base64 Message

```python
from decodify import decode_message

encoded_message = "aGVsbG8="
decoded, probabilities = decode_message(encoded_message)

print(f"Decoded Message: {decoded}")
# Output: Decoded Message: hello
print(f"Algorithm Probabilities: {probabilities}")
# Output: Algorithm Probabilities: {'base64': 1.0, ...}
```

### Decoding from a File

```bash
decodify encoded.txt -f
```

### Saving Decoded Output to a File

```bash
decodify "aGVsbG8=" --output decoded.txt
```

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## Issues

If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/ishanoshada/decodify).

---

## Acknowledgments

- Thanks to the Python community for creating amazing tools and libraries.
- Special thanks to contributors who helped improve this package.

---

## Contact

For questions or feedback, feel free to reach out:

- **Email**: ishan.kodithuwakku.offical@gmail.com
- **GitHub**: [ishanoshada](https://github.com/ishanoshada)

---

Enjoy decoding with **Decodify**! 🚀


**Repository Views** ![Views](https://profile-counter.glitch.me/decodify/count.svg)
