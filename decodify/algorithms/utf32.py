
# decodify/algorithms/utf32.py

def is_utf32(encoded: str) -> bool:
    try:
        if not encoded.strip():
            return False

        data = bytes.fromhex(encoded)

        if len(data) % 4:
            return False

        data.decode("utf-32-be")
        return True

    except (ValueError, UnicodeDecodeError):
        return False


def decode_utf32(encoded: str) -> str:
    try:
        data = bytes.fromhex(encoded)

        if len(data) % 4:
            raise ValueError("UTF-32 data must have a length divisible by 4")

        return data.decode("utf-32-be")

    except (ValueError, UnicodeDecodeError) as exc:
        raise ValueError("Invalid UTF-32 hexadecimal input") from exc


def encode_utf32(message: str) -> str:
    return message.encode("utf-32-be").hex()
