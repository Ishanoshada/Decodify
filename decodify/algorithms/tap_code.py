# decodify/algorithms/tap_code.py
"""Tap code - a 5x5 Polybius-style code tapped out as sounds/knocks (POW-camp cipher)."""

_SQUARE = [
    "ABCDE",
    "FGHIK",
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
    return pos_to_char, char_to_pos

_POS_TO_CHAR, _CHAR_TO_POS = _build_maps()

def is_tap_code(encoded: str) -> bool:
    """
    Check if the input looks like tap-code groups: pairs of dot-runs
    (1-5 dots each) separated by single spaces, letters separated by double spaces.
    """
    cleaned = encoded.strip()
    if not cleaned or set(cleaned) - set(". "):
        return False
    letter_groups = [g for g in cleaned.split("  ") if g]
    if not letter_groups:
        return False
    for group in letter_groups:
        taps = group.split()
        if len(taps) != 2:
            return False
        if not all(1 <= len(t) <= 5 for t in taps):
            return False
    return True

def decode_tap_code(encoded: str) -> str:
    """
    Decode a tap code string (double-space separated letter groups,
    each made of two single-space separated runs of dots).
    """
    letter_groups = [g for g in encoded.strip().split("  ") if g]
    result = []
    for group in letter_groups:
        taps = group.split()
        if len(taps) == 2:
            row, col = len(taps[0]), len(taps[1])
            result.append(_POS_TO_CHAR.get((row, col), "?"))
    return "".join(result)

def encode_tap_code(message: str) -> str:
    """
    Encode a string as tap code (I/J share a cell).
    """
    groups = []
    for c in message.upper():
        if c == "J":
            c = "I"
        if c in _CHAR_TO_POS:
            row, col = _CHAR_TO_POS[c]
            groups.append("." * row + " " + "." * col)
    return "  ".join(groups)
