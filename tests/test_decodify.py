
import pytest

from decodify import (
    decode_message,
    encode_message,
    list_algorithms,
)


# ============================================================================
# Original encoding algorithms
# ============================================================================

@pytest.mark.parametrize(
    "encoded, expected, algorithm",
    [
        ("aGVsbG8=", "hello", "base64"),
        ("68656c6c6f", "hello", "hex"),
        ("hello%20world", "hello world", "url"),
        (
            "01101000 01100101 01101100 01101100 01101111",
            "hello",
            "binary",
        ),
        (".... . .-.. .-.. ---", "HELLO", "morse"),
    ],
)
def test_decode_original_algorithms(encoded, expected, algorithm):
    decoded, probabilities = decode_message(
        encoded,
        algorithm=algorithm,
    )

    assert decoded == expected
    assert probabilities[algorithm] == 1.0


@pytest.mark.parametrize(
    "encoded, expected_algorithm",
    [
        ("aGVsbG8=", "base64"),
        ("68656c6c6f", "hex"),
        ("hello%20world", "url"),
        (
            "01101000 01100101 01101100 01101100 01101111",
            "binary",
        ),
        (".... . .-.. .-.. ---", "morse"),
    ],
)
def test_auto_detect_original_algorithms(encoded, expected_algorithm):
    _, probabilities = decode_message(encoded)

    assert probabilities[expected_algorithm] == pytest.approx(
        1.0,
        abs=0.01,
    )


# ============================================================================
# Unsupported and unknown input
# ============================================================================

def test_unsupported_encoding():
    encoded = "unsupported_encoding_xyz_12345_no_match"

    decoded, probabilities = decode_message(encoded)

    assert isinstance(decoded, str)
    assert isinstance(probabilities, dict)
    assert probabilities

    assert (
        "Unable to decode" in decoded
        or "Decode error" in decoded
        or decoded == encoded
        or all(score == 0.0 for score in probabilities.values())
        or max(probabilities.values()) < 0.5
    )


def test_empty_input():
    decoded, probabilities = decode_message("")

    assert isinstance(decoded, str)
    assert isinstance(probabilities, dict)


# ============================================================================
# Base encoding round-trip tests
# ============================================================================

@pytest.mark.parametrize(
    "algorithm, plaintext",
    [
        ("base32", "hello"),
        ("base58", "hello"),
        ("base85", "hello"),
        ("base45", "hello"),
        ("base36", "hello"),
        ("base64", "hello"),
        ("hex", "hello"),
        ("binary", "hello"),
        ("url", "hello world"),
    ],
)
def test_base_encoding_roundtrip(algorithm, plaintext):
    encoded = encode_message(plaintext, algorithm)

    assert isinstance(encoded, str)

    decoded, probabilities = decode_message(
        encoded,
        algorithm=algorithm,
    )

    assert decoded == plaintext
    assert probabilities[algorithm] == 1.0


# ============================================================================
# Classical cipher round-trip tests
# ============================================================================

def test_rot13_roundtrip():
    encoded = encode_message("hello", "rot13")

    assert encoded == "uryyb"

    decoded, _ = decode_message(
        encoded,
        algorithm="rot13",
    )

    assert decoded == "hello"


def test_rot47_roundtrip():
    encoded = encode_message("hello", "rot47")

    decoded, _ = decode_message(
        encoded,
        algorithm="rot47",
    )

    assert decoded == "hello"


def test_caesar_roundtrip():
    encoded = encode_message(
        "hello",
        "caesar",
        shift=3,
    )

    assert encoded == "khoor"

    decoded, _ = decode_message(
        encoded,
        algorithm="caesar",
        shift=3,
    )

    assert decoded == "hello"


def test_atbash_roundtrip():
    encoded = encode_message("hello", "atbash")

    assert encoded == "svool"

    decoded, _ = decode_message(
        encoded,
        algorithm="atbash",
    )

    assert decoded == "hello"


def test_vigenere_roundtrip():
    plaintext = "Attack at dawn"
    key = "LEMON"

    encoded = encode_message(
        plaintext,
        "vigenere",
        key=key,
    )

    decoded, _ = decode_message(
        encoded,
        algorithm="vigenere",
        key=key,
    )

    assert decoded == plaintext


def test_rail_fence_roundtrip():
    plaintext = "hello"

    encoded = encode_message(
        plaintext,
        "rail_fence",
        rails=3,
    )

    decoded, _ = decode_message(
        encoded,
        algorithm="rail_fence",
        rails=3,
    )

    assert decoded == plaintext


# ============================================================================
# XOR tests
# ============================================================================

def test_xor_roundtrip():
    plaintext = "secret"
    key = "key"

    encoded = encode_message(
        plaintext,
        "xor",
        key=key,
    )

    decoded, probabilities = decode_message(
        encoded,
        algorithm="xor",
        key=key,
    )

    assert decoded == plaintext
    assert probabilities["xor"] == 1.0


def test_xor_output_is_string():
    encoded = encode_message(
        "secret",
        "xor",
        key="key",
    )

    assert isinstance(encoded, str)


def test_xor_non_printable_output():
    encoded = encode_message(
        "secret",
        "xor",
        key="key",
    )

    assert encoded == "\x18\x00\x1a\x19\x00\r"

    decoded, _ = decode_message(
        encoded,
        algorithm="xor",
        key="key",
    )

    assert decoded == "secret"


def test_xor_different_keys():
    plaintext = "hello"

    encoded = encode_message(
        plaintext,
        "xor",
        key="key1",
    )

    decoded, _ = decode_message(
        encoded,
        algorithm="xor",
        key="key1",
    )

    assert decoded == plaintext


# ============================================================================
# Additional classical ciphers
# ============================================================================

def test_affine_roundtrip():
    plaintext = "hello"

    encoded = encode_message(
        plaintext,
        "affine",
        a=5,
        b=8,
    )

    decoded, _ = decode_message(
        encoded,
        algorithm="affine",
        a=5,
        b=8,
    )

    assert decoded == plaintext


# ============================================================================
# Historical and specialty encodings
# ============================================================================

@pytest.mark.parametrize(
    "algorithm, plaintext, expected",
    [
        ("baconian", "hello", "HELLO"),
        ("polybius", "hello", "HELLO"),
        ("tap_code", "hi", "HI"),
        ("nato", "sos", "SOS"),
        ("brainfuck", "hi", "hi"),
    ],
)
def test_specialty_algorithm_roundtrip(
    algorithm,
    plaintext,
    expected,
):
    encoded = encode_message(plaintext, algorithm)

    decoded, _ = decode_message(
        encoded,
        algorithm=algorithm,
    )

    assert decoded == expected


# ============================================================================
# Text and web encodings
# ============================================================================

@pytest.mark.parametrize(
    "algorithm, plaintext",
    [
        ("quoted_printable", "café = test"),
        ("html_entities", "<script>alert(1)</script>"),
        ("unicode_escape", "café"),
        ("uuencode", "hello"),
        ("punycode", "münchen.de"),
    ],
)
def test_text_encoding_roundtrip(algorithm, plaintext):
    encoded = encode_message(
        plaintext,
        algorithm,
    )

    decoded, _ = decode_message(
        encoded,
        algorithm=algorithm,
    )

    assert decoded == plaintext


def test_jwt_decode():
    encoded = encode_message(
        '{"sub":"test"}',
        "jwt",
    )

    decoded, probabilities = decode_message(
        encoded,
        algorithm="jwt",
    )

    assert "header" in decoded
    assert "payload" in decoded
    assert probabilities["jwt"] == 1.0


# ============================================================================
# Auto-detection for distinctive formats
# ============================================================================

@pytest.mark.parametrize(
    "algorithm, plaintext",
    [
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
    ],
)
def test_auto_detect_distinctive_formats(algorithm, plaintext):
    encoded = encode_message(
        plaintext,
        algorithm,
    )

    decoded, probabilities = decode_message(encoded)

    assert isinstance(decoded, str)
    assert isinstance(probabilities, dict)

    highest_algorithm = max(
        probabilities,
        key=probabilities.get,
    )

    assert (
        highest_algorithm == algorithm
        or probabilities.get(algorithm, 0.0) > 0.3
    )

    assert (
        decoded.lower().replace(" ", "")
        == plaintext.lower().replace(" ", "")
        or plaintext.lower() in decoded.lower()
    )


# ============================================================================
# Algorithm listing
# ============================================================================

def test_list_algorithms():
    algorithms = list_algorithms()

    assert isinstance(algorithms, list)
    assert len(algorithms) >= 25

    required_algorithms = [
        "base64",
        "hex",
        "morse",
        "base32",
        "base58",
        "base85",
        "base45",
        "base36",
        "caesar",
        "rot13",
        "rot47",
        "vigenere",
        "xor",
        "jwt",
        "brainfuck",
    ]

    for algorithm in required_algorithms:
        assert algorithm in algorithms


def test_list_algorithms_unique():
    algorithms = list_algorithms()

    assert len(algorithms) == len(set(algorithms))


# ============================================================================
# Public encode API
# ============================================================================

def test_encode_message_api():
    assert encode_message(
        "hello",
        "base64",
    ) == "aGVsbG8="

    assert encode_message(
        "hello",
        "hex",
    ) == "68656c6c6f"

    nato = encode_message("a", "nato")

    assert "Alpha" in nato or "ALPHA" in nato.upper()


def test_encode_message_returns_string():
    encoded = encode_message(
        "hello",
        "base64",
    )

    assert isinstance(encoded, str)


# ============================================================================
# CLI tests
# ============================================================================

def test_file_decoding(tmp_path, monkeypatch, capsys):
    encoded_file = tmp_path / "encoded.txt"

    encoded_file.write_text(
        "aGVsbG8=",
        encoding="utf-8",
    )

    from decodify.cli import main

    monkeypatch.setattr(
        "sys.argv",
        ["decodify", str(encoded_file), "-f"],
    )

    main()

    output = capsys.readouterr().out

    assert "Decoded Message: hello" in output
    assert "Algorithm Probabilities:" in output
    assert "base64" in output


def test_cli_with_algorithm(tmp_path, monkeypatch, capsys):
    encoded_file = tmp_path / "encoded.txt"

    encoded_file.write_text(
        "aGVsbG8=",
        encoding="utf-8",
    )

    from decodify.cli import main

    monkeypatch.setattr(
        "sys.argv",
        [
            "decodify",
            str(encoded_file),
            "-f",
            "--algorithm",
            "base64",
        ],
    )

    main()

    output = capsys.readouterr().out

    assert "Decoded Message: hello" in output
    assert "base64" in output


def test_cli_output_file(tmp_path, monkeypatch, capsys):
    encoded_file = tmp_path / "encoded.txt"
    output_file = tmp_path / "decoded.txt"

    encoded_file.write_text(
        "aGVsbG8=",
        encoding="utf-8",
    )

    from decodify.cli import main

    monkeypatch.setattr(
        "sys.argv",
        [
            "decodify",
            str(encoded_file),
            "-f",
            "--output",
            str(output_file),
        ],
    )

    main()

    output = capsys.readouterr().out

    assert (
        "saved" in output.lower()
        or "Decoded Message" in output
    )

    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8").strip() == "hello"


def test_cli_list(monkeypatch, capsys):
    from decodify.cli import main

    monkeypatch.setattr(
        "sys.argv",
        ["decodify", "--list"],
    )

    main()

    output = capsys.readouterr().out

    assert "base64" in output
    assert "morse" in output
    assert "brainfuck" in output


# ============================================================================
# Package API consistency
# ============================================================================

def test_decode_message_return_structure():
    decoded, probabilities = decode_message(
        "aGVsbG8=",
        algorithm="base64",
    )

    assert isinstance(decoded, str)
    assert isinstance(probabilities, dict)


def test_probability_values_are_numeric():
    _, probabilities = decode_message(
        "aGVsbG8=",
    )

    for algorithm, probability in probabilities.items():
        assert isinstance(algorithm, str)
        assert isinstance(probability, (int, float))


def test_probability_values_are_in_range():
    _, probabilities = decode_message(
        "aGVsbG8=",
    )

    for probability in probabilities.values():
        assert 0.0 <= probability <= 1.0
