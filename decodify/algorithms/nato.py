# decodify/algorithms/nato.py
NATO = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee",
    "Z": "Zulu",
    "0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four",
    "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine",
}
REVERSE = {v.upper(): k for k, v in NATO.items()}
# also accept common variants
REVERSE["XRAY"] = "X"
REVERSE["JULIETT"] = "J"

def is_nato(encoded: str) -> bool:
    """
    Check if input consists of NATO phonetic words.
    """
    words = encoded.strip().upper().split()
    if not words:
        return False
    hits = sum(1 for w in words if w in REVERSE or w.replace("-", "") in REVERSE)
    return hits / len(words) > 0.6

def decode_nato(encoded: str) -> str:
    """
    Decode NATO phonetic alphabet to letters.
    """
    words = encoded.strip().upper().replace("-", "").split()
    result = []
    for w in words:
        result.append(REVERSE.get(w, "?"))
    return "".join(result)

def encode_nato(message: str) -> str:
    """
    Encode to NATO phonetic alphabet.
    """
    parts = []
    for c in message.upper():
        if c in NATO:
            parts.append(NATO[c])
        elif c == " ":
            parts.append("/")
    return " ".join(parts)
