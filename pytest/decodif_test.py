import pytest
from decodify import decode_message, detect_algorithm

# Test cases for each algorithm
@pytest.mark.parametrize("encoded, expected_decoded, expected_algorithm", [
    # Base64
    ("aGVsbG8=", "hello", "base64"),
    # Hexadecimal
    ("68656c6c6f", "hello", "hex"),
    # URL Encoding
    ("hello%20world", "hello world", "url"),
    # Binary
    ("01101000 01100101 01101100 01101100 01101111", "hello", "binary"),
    # Morse Code
    (".... . .-.. .-.. ---", "HELLO", "morse"),
])
def test_decode_message(encoded, expected_decoded, expected_algorithm):
    """
    Test the decode_message function for various encoding algorithms.
    """
    decoded, probabilities = decode_message(encoded, algorithm=expected_algorithm)
    assert decoded == expected_decoded
    assert probabilities[expected_algorithm] == 1.0

# Test detection mechanism
@pytest.mark.parametrize("encoded, expected_algorithm", [
    # Base64
    ("aGVsbG8=", "base64"),
    # Hexadecimal
    ("68656c6c6f", "hex"),
    # URL Encoding
    ("hello%20world", "url"),
    # Binary
    ("01101000 01100101 01101100 01101100 01101111", "binary"),
    # Morse Code
    (".... . .-.. .-.. ---", "morse"),
])
def test_detect_algorithm(encoded, expected_algorithm):
    """
    Test the detect_algorithm function for various encoding algorithms.
    """
    _, probabilities = decode_message(encoded)
    assert probabilities[expected_algorithm] == 1.0

# Test unsupported encoding
def test_unsupported_encoding():
    """
    Test the decode_message function with an unsupported encoding.
    """
    encoded = "unsupported_encoding"
    decoded, probabilities = decode_message(encoded)
    assert decoded == "Unable to decode the message."
    assert all(prob == 0.0 for prob in probabilities.values())

# Test file decoding (CLI functionality)
def test_file_decoding(tmp_path):
    """
    Test decoding a message from a file.
    """
    # Create a temporary file with encoded message
    encoded_message = "aGVsbG8="
    file_path = tmp_path / "encoded.txt"
    file_path.write_text(encoded_message)

    # Simulate CLI functionality
    from decodify.cli import main
    import sys
    from io import StringIO

    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate CLI arguments
    sys.argv = ["decodify", str(file_path), "-f"]
    main()

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue()
    assert "Decoded Message: hello" in output
    assert "Algorithm Probabilities:" in output
    assert "base64: 1.00" in output

# Test CLI with algorithm specified
def test_cli_with_algorithm(tmp_path):
    """
    Test the CLI with a specified algorithm.
    """
    # Create a temporary file with encoded message
    encoded_message = "aGVsbG8="
    file_path = tmp_path / "encoded.txt"
    file_path.write_text(encoded_message)

    # Simulate CLI functionality
    from decodify.cli import main
    import sys
    from io import StringIO

    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate CLI arguments
    sys.argv = ["decodify", str(file_path), "-f", "--algorithm", "base64"]
    main()

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue()
    assert "Decoded Message: hello" in output
    assert "Algorithm Probabilities:" in output
    assert "base64: 1.00" in output

# Test CLI with output file
def test_cli_output_file(tmp_path):
    """
    Test the CLI with output saved to a file.
    """
    # Create a temporary file with encoded message
    encoded_message = "aGVsbG8="
    file_path = tmp_path / "encoded.txt"
    file_path.write_text(encoded_message)

    # Output file path
    output_file = tmp_path / "decoded.txt"

    # Simulate CLI functionality
    from decodify.cli import main
    import sys
    from io import StringIO

    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    # Simulate CLI arguments
    sys.argv = ["decodify", str(file_path), "-f", "--output", str(output_file)]
    main()

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Check output
    output = captured_output.getvalue()
    assert "Decoded message saved to" in output

    # Check the content of the output file
    with open(output_file, "r") as f:
        assert f.read().strip() == "hello"