import pytest
from decodify import decode_message, encode_message, detect_algorithm, list_algorithms


# ---------------------------------------------------------------------------
# Original algorithm tests (forced algorithm)
# ---------------------------------------------------------------------------
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
def test_decode_message_original(encoded, expected_decoded, expected_algorithm):
    decoded, probabilities = decode_message(encoded, algorithm=expected_algorithm)
    assert decoded == expected_decoded
    assert probabilities[expected_algorithm] == 1.0


# ---------------------------------------------------------------------------
# Auto-detection for original algorithms
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("encoded, expected_algorithm", [
    ("aGVsbG8=", "base64"),
    ("68656c6c6f", "hex"),
    ("hello%20world", "url"),
    ("01101000 01100101 01101100 01101100 01101111", "binary"),
    (".... . .-.. .-.. ---", "morse"),
])
def test_detect_algorithm_original(encoded, expected_algorithm):
    _, probabilities = decode_message(encoded)
    assert probabilities[expected_algorithm] == pytest.approx(1.0, abs=0.01)


# ---------------------------------------------------------------------------
# Unsupported / unknown input
# ---------------------------------------------------------------------------
def test_unsupported_encoding():
    encoded = "unsupported_encoding_xyz_12345_no_match"
    decoded, probabilities = decode_message(encoded)
    # Should not successfully decode to a sensible plaintext
    # (may attempt base64 and fail with a decode error, or return unable)
    assert (
        "Unable to decode" in decoded
        or "Decode error" in decoded
        or all(p == 0.0 for p in probabilities.values())
        or max(probabilities.values()) < 0.5
        or decoded == encoded  # no change
    )


# ---------------------------------------------------------------------------
# New base encodings – forced decode
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("algorithm, plaintext", [
    ("base32", "hello"),
    ("base58", "hello"),
    ("base85", "hello"),
    ("base45", "hello"),
    ("base36", "hello"),
])
def test_new_base_encodings_roundtrip(algorithm, plaintext):
    encoded = encode_message(plaintext, algorithm)
    decoded, probs = decode_message(encoded, algorithm=algorithm)
    assert decoded == plaintext
    assert probs[algorithm] == 1.0


# ---------------------------------------------------------------------------
# Classical ciphers – forced decode with keys
# ---------------------------------------------------------------------------
def test_rot13_roundtrip():
    encoded = encode_message("hello", "rot13")
    assert encoded == "uryyb"
    decoded, _ = decode_message(encoded, algorithm="rot13")
    assert decoded == "hello"


def test_rot47_roundtrip():
    encoded = encode_message("hello", "rot47")
    decoded, _ = decode_message(encoded, algorithm="rot47")
    assert decoded == "hello"


def test_caesar_roundtrip():
    encoded = encode_message("hello", "caesar", shift=3)
    assert encoded == "khoor"
    decoded, _ = decode_message(encoded, algorithm="caesar", shift=3)
    assert decoded == "hello"


def test_atbash_roundtrip():
    encoded = encode_message("hello", "atbash")
    assert encoded == "svool"
    decoded, _ = decode_message(encoded, algorithm="atbash")
    assert decoded == "hello"


def test_vigenere_roundtrip():
    encoded = encode_message("hello", "vigenere", key="KEY")
    decoded, _ = decode_message(encoded, algorithm="vigenere", key="KEY")
    assert decoded == "hello"


def test_rail_fence_roundtrip():
    encoded = encode_message("hello", "rail_fence", rails=3)
    decoded, _ = decode_message(encoded, algorithm="rail_fence", rails=3)
    assert decoded == "hello"


def test_xor_roundtrip():
    encoded = encode_message("hello", "xor", key="k")
    decoded, _ = decode_message(encoded, algorithm="xor", key="k")
    assert decoded == "hello"


def test_affine_roundtrip():
    encoded = encode_message("hello", "affine", a=5, b=8)
    decoded, _ = decode_message(encoded, algorithm="affine", a=5, b=8)
    assert decoded == "hello"


# ---------------------------------------------------------------------------
# Historical / specialty
# ---------------------------------------------------------------------------
def test_baconian_roundtrip():
    encoded = encode_message("hello", "baconian")
    decoded, _ = decode_message(encoded, algorithm="baconian")
    assert decoded == "HELLO"


def test_polybius_roundtrip():
    encoded = encode_message("hello", "polybius")
    decoded, _ = decode_message(encoded, algorithm="polybius")
    assert decoded == "HELLO"


def test_tap_code_roundtrip():
    encoded = encode_message("hi", "tap_code")
    decoded, _ = decode_message(encoded, algorithm="tap_code")
    assert decoded == "HI"


def test_nato_roundtrip():
    encoded = encode_message("sos", "nato")
    decoded, _ = decode_message(encoded, algorithm="nato")
    assert decoded == "SOS"


def test_brainfuck_roundtrip():
    encoded = encode_message("hi", "brainfuck")
    decoded, _ = decode_message(encoded, algorithm="brainfuck")
    assert decoded == "hi"


# ---------------------------------------------------------------------------
# Text / web encodings
# ---------------------------------------------------------------------------
def test_quoted_printable_roundtrip():
    plaintext = "café = test"
    encoded = encode_message(plaintext, "quoted_printable")
    decoded, _ = decode_message(encoded, algorithm="quoted_printable")
    assert decoded == plaintext


def test_html_entities_roundtrip():
    plaintext = "<script>alert(1)</script>"
    encoded = encode_message(plaintext, "html_entities")
    decoded, _ = decode_message(encoded, algorithm="html_entities")
    assert decoded == plaintext


def test_unicode_escape_roundtrip():
    plaintext = "café"
    encoded = encode_message(plaintext, "unicode_escape")
    decoded, _ = decode_message(encoded, algorithm="unicode_escape")
    assert decoded == plaintext


def test_uuencode_roundtrip():
    plaintext = "hello"
    encoded = encode_message(plaintext, "uuencode")
    decoded, _ = decode_message(encoded, algorithm="uuencode")
    assert decoded == plaintext


def test_punycode_roundtrip():
    plaintext = "münchen.de"
    encoded = encode_message(plaintext, "punycode")
    decoded, _ = decode_message(encoded, algorithm="punycode")
    assert decoded == plaintext


def test_jwt_decode():
    token = encode_message('{"sub":"test"}', "jwt")
    decoded, probs = decode_message(token, algorithm="jwt")
    assert "header" in decoded
    assert "payload" in decoded
    assert probs["jwt"] == 1.0


# ---------------------------------------------------------------------------
# Auto-detection for distinctive new formats
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("algorithm, plaintext", [
    ("base32", "hello"),
    ("base58", "hello"),
    ("base85", "hello"),
    ("base45", "hello"),
    ("nato", "sos"),
    ("tap_code", "hi"),
    ("polybius", "help"),
    ("baconian", "hello"),
    ("brainfuck", "hi"),
    ("morse", "sos"),
])
def test_auto_detect_distinctive(algorithm, plaintext):
    encoded = encode_message(plaintext, algorithm)
    decoded, probs = decode_message(encoded)  # no algorithm forced
    top = max(probs, key=probs.get)
    assert top == algorithm or probs.get(algorithm, 0) > 0.3
    assert (
        decoded.lower().replace(" ", "") == plaintext.lower().replace(" ", "")
        or plaintext.lower() in decoded.lower()
    )


# ---------------------------------------------------------------------------
# list_algorithms
# ---------------------------------------------------------------------------
def test_list_algorithms():
    algs = list_algorithms()
    assert isinstance(algs, list)
    assert len(algs) >= 25
    for required in ["base64", "hex", "morse", "base32", "caesar", "jwt", "brainfuck"]:
        assert required in algs


# ---------------------------------------------------------------------------
# Encode API
# ---------------------------------------------------------------------------
def test_encode_message_api():
    assert encode_message("hello", "base64") == "aGVsbG8="
    assert encode_message("hello", "hex") == "68656c6c6f"
    nato = encode_message("a", "nato")
    assert "Alpha" in nato or "ALPHA" in nato.upper()


# ---------------------------------------------------------------------------
# CLI tests
# ---------------------------------------------------------------------------
def test_file_decoding(tmp_path):
    encoded_message = "aGVsbG8="
    file_path = tmp_path / "encoded.txt"
    file_path.write_text(encoded_message)

    from decodify.cli import main
    import sys
    from io import StringIO

    captured_output = StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured_output
    old_argv = sys.argv
    try:
        sys.argv = ["decodify", str(file_path), "-f"]
        main()
    finally:
        sys.stdout = old_stdout
        sys.argv = old_argv

    output = captured_output.getvalue()
    assert "Decoded Message: hello" in output
    assert "Algorithm Probabilities:" in output
    assert "base64" in output


def test_cli_with_algorithm(tmp_path):
    encoded_message = "aGVsbG8="
    file_path = tmp_path / "encoded.txt"
    file_path.write_text(encoded_message)

    from decodify.cli import main
    import sys
    from io import StringIO

    captured_output = StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured_output
    old_argv = sys.argv
    try:
        sys.argv = ["decodify", str(file_path), "-f", "--algorithm", "base64"]
        main()
    finally:
        sys.stdout = old_stdout
        sys.argv = old_argv

    output = captured_output.getvalue()
    assert "Decoded Message: hello" in output
    assert "base64" in output


def test_cli_output_file(tmp_path):
    encoded_message = "aGVsbG8="
    file_path = tmp_path / "encoded.txt"
    file_path.write_text(encoded_message)
    output_file = tmp_path / "decoded.txt"

    from decodify.cli import main
    import sys
    from io import StringIO

    captured_output = StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured_output
    old_argv = sys.argv
    try:
        sys.argv = ["decodify", str(file_path), "-f", "--output", str(output_file)]
        main()
    finally:
        sys.stdout = old_stdout
        sys.argv = old_argv

    output = captured_output.getvalue()
    assert "saved" in output.lower() or "Decoded Message" in output
    assert output_file.read_text().strip() == "hello"


def test_cli_list():
    from decodify.cli import main
    import sys
    from io import StringIO

    captured_output = StringIO()
    old_stdout = sys.stdout
    sys.stdout = captured_output
    old_argv = sys.argv
    try:
        sys.argv = ["decodify", "--list"]
        main()
    finally:
        sys.stdout = old_stdout
        sys.argv = old_argv

    output = captured_output.getvalue()
    assert "base64" in output
    assert "morse" in output
    assert "brainfuck" in output