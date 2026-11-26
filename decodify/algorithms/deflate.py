
# decodify/algorithms/deflate.py

import base64
import zlib


def encode_deflate(message: str) -> str:
    compressor = zlib.compressobj(
        level=9,
        wbits=-zlib.MAX_WBITS
    )

    compressed = (
        compressor.compress(message.encode("utf-8"))
        + compressor.flush()
    )

    return base64.b64encode(compressed).decode("ascii")


def decode_deflate(encoded: str) -> str:
    try:
        compressed = base64.b64decode(encoded, validate=True)

        decompressor = zlib.decompressobj(
            wbits=-zlib.MAX_WBITS
        )

        data = decompressor.decompress(compressed)
        data += decompressor.flush()

        if not decompressor.eof or decompressor.unused_data:
            raise ValueError("Invalid or incomplete DEFLATE stream")

        return data.decode("utf-8")

    except Exception as exc:
        raise ValueError("Invalid DEFLATE input") from exc


def is_deflate(encoded: str) -> bool:
    try:
        decode_deflate(encoded)
        return True
    except (ValueError, TypeError):
        return False
