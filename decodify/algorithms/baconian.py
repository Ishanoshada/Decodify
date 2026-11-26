# decodify/algorithms/baconian.py
# 24-letter Baconian (I/J and U/V combined)
_BACON = {
    "AAAAA": "A", "AAAAB": "B", "AAABA": "C", "AAABB": "D", "AABAA": "E",
    "AABAB": "F", "AABBA": "G", "AABBB": "H", "ABAAA": "I", "ABAAB": "K",
    "ABABA": "L", "ABABB": "M", "ABBAA": "N", "ABBAB": "O", "ABBBA": "P",
    "ABBBB": "Q", "BAAAA": "R", "BAAAB": "S", "BAABA": "T", "BAABB": "U",
    "BABAA": "W", "BABAB": "X", "BABBA": "Y", "BABBB": "Z",
}
_CHAR_TO_BACON = {v: k for k, v in _BACON.items()}
_CHAR_TO_BACON["J"] = "ABAAA"  # same as I
_CHAR_TO_BACON["V"] = "BAABB"  # same as U

def is_baconian(encoded: str) -> bool:
    """
    Check for groups of 5 A/B characters.
    """
    cleaned = encoded.strip().upper().replace(" ", "")
    if not cleaned or len(cleaned) % 5 != 0:
        return False
    return all(c in "AB" for c in cleaned)

def decode_baconian(encoded: str) -> str:
    """
    Decode Baconian cipher (A/B groups of 5).
    """
    cleaned = encoded.strip().upper().replace(" ", "")
    result = []
    for i in range(0, len(cleaned), 5):
        group = cleaned[i:i+5]
        result.append(_BACON.get(group, "?"))
    return "".join(result)

def encode_baconian(message: str) -> str:
    """
    Encode to Baconian cipher.
    """
    groups = []
    for c in message.upper():
        if c in _CHAR_TO_BACON:
            groups.append(_CHAR_TO_BACON[c])
    return " ".join(groups)
