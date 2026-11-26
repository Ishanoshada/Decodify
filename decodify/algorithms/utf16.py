
# decodify/algorithms/utf16.py

def is_utf16(encoded: str) -> bool:
    try:
        if not encoded.strip():
            return False

        data = bytes.fromhex(encoded)

        if len(data) % 2:
            return False

        data.decode("utf-16-be")
        return True

    except (ValueError, UnicodeDecodeError):
        return False


def decode_utf16(encoded: str) -> str:
    try:
        data = bytes.fromhex(encoded)

        if len(data) % 2:
            raise ValueError("UTF-16 data must have an even byte length")

        return data.decode("utf-16-be")

    except (ValueError, UnicodeDecodeError) as exc:
        raise ValueError("Invalid UTF-16 hexadecimal input") from exc


def encode_utf16(message: str) -> str:
    return message.encode("utf-16-be").hex()
