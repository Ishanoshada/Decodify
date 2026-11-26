# decodify/decodify.py
from typing import Dict, Tuple, Optional, Any
from .algorithms import ALGORITHMS

class Decodify:
    # Specificity / priority weights (higher = preferred when multiple match)
    SPECIFICITY = {
        "jwt": 5.0,
        "uuencode": 4.5,
        "punycode": 4.0,
        "brainfuck": 4.0,
        "tap_code": 3.5,
        "baconian": 3.0,
        "polybius": 3.0,
        "morse": 3.0,
        "nato": 2.8,
        "base45": 2.2,
        "base85": 2.2,
        "base58": 2.0,
        "base32": 1.8,
        "base64": 1.7,
        "unicode_escape": 2.0,
        "html_entities": 1.8,
        "quoted_printable": 1.6,
        "hex": 1.5,
        "binary": 1.5,
        "url": 1.4,
        "base36": 1.2,
        # weak / ambiguous – only win when nothing better matches
        "rot13": 0.3,
        "rot47": 0.3,
        "caesar": 0.25,
        "atbash": 0.25,
        "vigenere": 0.2,
        "rail_fence": 0.2,
        "xor": 0.15,
        "affine": 0.2,
    }

    @staticmethod
    def detect_algorithm(encoded: str) -> Dict[str, float]:
        """
        Detect the likelihood of each encoding algorithm being used.
        """
        raw = {}
        for name, (is_fn, _, _) in ALGORITHMS.items():
            try:
                raw[name] = 1.0 if is_fn(encoded) else 0.0
            except Exception:
                raw[name] = 0.0

        weighted = {
            name: score * Decodify.SPECIFICITY.get(name, 1.0)
            for name, score in raw.items()
        }

        total = sum(weighted.values())
        if total > 0:
            for k in weighted:
                weighted[k] /= total
        else:
            for k in weighted:
                weighted[k] = 0.0
        return weighted

    @staticmethod
    def decode_message(
        encoded: str,
        algorithm: Optional[str] = None,
        **kwargs: Any,
    ) -> Tuple[str, Dict[str, float]]:
        """
        Decode the message using the specified algorithm or by detecting the most likely one.
        Extra kwargs are passed to keyed algorithms (key=, shift=, rails=, a=, b=).
        """
        if algorithm:
            algorithm = algorithm.lower().replace("-", "_")
            if algorithm not in ALGORITHMS:
                return f"Unsupported algorithm: {algorithm}", {algorithm: 0.0}
            _, decode_fn, _ = ALGORITHMS[algorithm]
            try:
                decoded = Decodify._call_decode(decode_fn, algorithm, encoded, kwargs)
            except Exception as e:
                decoded = f"Decode error ({algorithm}): {e}"
            return decoded, {algorithm: 1.0}

        # Auto-detect
        probs = Decodify.detect_algorithm(encoded)
        most_likely = max(probs, key=probs.get)

        if probs[most_likely] == 0.0:
            return "Unable to decode the message. No known encoding detected.", probs

        _, decode_fn, _ = ALGORITHMS[most_likely]
        try:
            decoded = Decodify._call_decode(decode_fn, most_likely, encoded, kwargs)
        except Exception as e:
            # fall back to next best if decode fails
            candidates = sorted(probs.items(), key=lambda x: -x[1])
            decoded = f"Decode error ({most_likely}): {e}"
            for name, p in candidates[1:]:
                if p <= 0:
                    break
                try:
                    _, fn, _ = ALGORITHMS[name]
                    decoded = Decodify._call_decode(fn, name, encoded, kwargs)
                    # update so caller sees which one actually worked
                    probs = {n: (1.0 if n == name else 0.0) for n in probs}
                    break
                except Exception:
                    continue

        return decoded, probs

    @staticmethod
    def _call_decode(fn, name, encoded, kwargs):
        if name == "caesar":
            return fn(encoded, shift=kwargs.get("shift", 3))
        if name == "vigenere":
            return fn(encoded, key=kwargs.get("key", "KEY"))
        if name == "rail_fence":
            return fn(encoded, rails=kwargs.get("rails", 3))
        if name == "xor":
            return fn(encoded, key=kwargs.get("key", "key"))
        if name == "affine":
            return fn(encoded, a=kwargs.get("a", 5), b=kwargs.get("b", 8))
        return fn(encoded)

    @staticmethod
    def encode_message(message: str, algorithm: str, **kwargs: Any) -> str:
        """
        Encode a message with the given algorithm.
        """
        algorithm = algorithm.lower().replace("-", "_")
        if algorithm not in ALGORITHMS:
            return f"Unsupported algorithm: {algorithm}"
        _, _, encode_fn = ALGORITHMS[algorithm]
        try:
            if algorithm == "caesar":
                return encode_fn(message, shift=kwargs.get("shift", 3))
            if algorithm == "vigenere":
                return encode_fn(message, key=kwargs.get("key", "KEY"))
            if algorithm == "rail_fence":
                return encode_fn(message, rails=kwargs.get("rails", 3))
            if algorithm == "xor":
                return encode_fn(message, key=kwargs.get("key", "key"))
            if algorithm == "affine":
                return encode_fn(message, a=kwargs.get("a", 5), b=kwargs.get("b", 8))
            return encode_fn(message)
        except Exception as e:
            return f"Encode error ({algorithm}): {e}"

    @staticmethod
    def list_algorithms() -> list:
        """Return sorted list of supported algorithm names."""
        return sorted(ALGORITHMS.keys())
