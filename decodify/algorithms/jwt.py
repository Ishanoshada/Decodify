# decodify/algorithms/jwt.py
import base64
import json
import re

def is_jwt(encoded: str) -> bool:
    """
    Check for three base64url parts separated by dots.
    """
    parts = encoded.strip().split(".")
    if len(parts) != 3:
        return False
    # header and payload should look base64url
    for p in parts[:2]:
        if not re.match(r"^[A-Za-z0-9_-]+$", p):
            return False
    return True

def decode_jwt(encoded: str) -> str:
    """
    Decode JWT header + payload (no signature verification).
    Returns pretty JSON of header and payload.
    """
    parts = encoded.strip().split(".")
    if len(parts) < 2:
        return "Invalid JWT"
    def b64url_decode(s):
        pad = 4 - len(s) % 4
        if pad != 4:
            s += "=" * pad
        return base64.urlsafe_b64decode(s)
    try:
        header = json.loads(b64url_decode(parts[0]))
        payload = json.loads(b64url_decode(parts[1]))
        return json.dumps({"header": header, "payload": payload}, indent=2)
    except Exception as e:
        return f"JWT decode error: {e}"

def encode_jwt(message: str) -> str:
    """
    Not a real JWT signer; just notes that signing requires a key.
    For demo, treat message as payload claim.
    """
    header = base64.urlsafe_b64encode(b'{"alg":"none","typ":"JWT"}').decode().rstrip("=")
    try:
        payload_obj = json.loads(message)
    except Exception:
        payload_obj = {"data": message}
    payload = base64.urlsafe_b64encode(json.dumps(payload_obj).encode()).decode().rstrip("=")
    return f"{header}.{payload}."
