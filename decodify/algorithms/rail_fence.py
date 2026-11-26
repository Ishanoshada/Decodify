# decodify/algorithms/rail_fence.py
def is_rail_fence(encoded: str) -> bool:
    """Weak cipher – detection disabled; user must specify algorithm."""
    return False
    # original logic kept below for reference
    """
    Weak detection for rail fence.
    """
    return bool(encoded.strip()) and len(encoded) > 3

def decode_rail_fence(encoded: str, rails: int = 3) -> str:
    """
    Decode Rail Fence cipher with given number of rails.
    """
    if rails < 2:
        return encoded
    n = len(encoded)
    # Build the fence pattern
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for i in range(n):
        fence[rail].append(i)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    # Place characters
    pos = 0
    result = [""] * n
    for r in range(rails):
        for idx in fence[r]:
            result[idx] = encoded[pos]
            pos += 1
    return "".join(result)

def encode_rail_fence(message: str, rails: int = 3) -> str:
    """
    Encode with Rail Fence cipher.
    """
    if rails < 2:
        return message
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for c in message:
        fence[rail].append(c)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
    return "".join("".join(row) for row in fence)
