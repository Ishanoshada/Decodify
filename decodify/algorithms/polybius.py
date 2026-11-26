# decodify/algorithms/polybius.py
_SQUARE = [
    "ABCDE",
    "FGHIK",  # J omitted / merged with I
    "LMNOP",
    "QRSTU",
    "VWXYZ",
]

def _build_maps():
    pos_to_char = {}
    char_to_pos = {}
    for r, row in enumerate(_SQUARE):
        for c, ch in enumerate(row):
            pos_to_char[(r + 1, c + 1)] = ch
            char_to_pos[ch] = (r + 1, c + 1)
    char_to_pos["J"] = char_to_pos["I"]
    return pos_to_char, char_to_pos

_POS_TO_CHAR, _CHAR_TO_POS = _build_maps()

def is_polybius(encoded: str) -> bool:
    """
    Check for pairs of digits 1-5.
    """
    cleaned = encoded.strip().replace(" ", "")
    if not cleaned or len(cleaned) % 2 != 0:
        return False
    return all(c in "12345" for c in cleaned)

def decode_polybius(encoded: str) -> str:
    """
    Decode Polybius square (pairs of 1-5).
    """
    cleaned = encoded.strip().replace(" ", "")
    result = []
    for i in range(0, len(cleaned), 2):
        row = int(cleaned[i])
        col = int(cleaned[i+1])
        result.append(_POS_TO_CHAR.get((row, col), "?"))
    return "".join(result)

def encode_polybius(message: str) -> str:
    """
    Encode with Polybius square.
    """
    pairs = []
    for c in message.upper():
        if c == "J":
            c = "I"
        if c in _CHAR_TO_POS:
            r, col = _CHAR_TO_POS[c]
            pairs.append(f"{r}{col}")
    return " ".join(pairs)
