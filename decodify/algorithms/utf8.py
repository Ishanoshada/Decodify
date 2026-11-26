
# decodify/algorithms/utf8.py

def is_utf8(encoded: str) -> bool:
    try:
        if not encoded.strip():
            return False
        bytes.fromhex(encoded).decode("utf-8")
        return True
    except (ValueError, UnicodeDecodeError):
        return False


def decode_utf8(encoded: str) -> str:
    try:
        return bytes.fromhex(encoded).decode("utf-8")
    except (ValueError, UnicodeDecodeError) as exc:
        raise ValueError("Invalid UTF-8 hexadecimal input") from exc


def encode_utf8(message: str) -> str:
    return message.encode("utf-8").hex()
