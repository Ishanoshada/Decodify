
from typing import Dict, Tuple, Optional, Any

from .algorithms import ALGORITHMS


class Decodify:
    """Main Decodify encoding, decoding, and detection interface."""

    # Specificity weights for automatic detection.
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
        "base64url": 1.7,
        "base32hex": 1.7,
        "base91": 2.0,
        "z85": 2.0,
        "unicode_escape": 2.0,
        "html_entities": 1.8,
        "html_decimal": 1.8,
        "html_hex": 1.8,
        "quoted_printable": 1.6,
        "hex": 1.5,
        "binary": 1.5,
        "url": 1.4,
        "base36": 1.2,
        "decimal": 1.2,
        "octal": 1.2,
        "utf8": 1.2,
        "utf16": 1.2,
        "utf32": 1.2,
        "gzip": 1.5,
        "zlib": 1.5,
        "bz2": 1.5,
        "lzma": 1.5,
        "deflate": 1.5,
        "escape": 1.5,
        "ascii": 1.0,
    }

    # Algorithms requiring explicit parameters.
    REQUIRED_PARAMETERS = {
        "autokey": ("key",),
        "beaufort": ("key",),
        "gronsfeld": ("key",),
        "porta": ("key",),
        "columnar_transposition": ("key",),
        "hill": ("key",),
        "playfair": ("key",),
        "scytale": ("key",),
        "substitution": ("key",),
    }

    # Ambiguous algorithms are excluded from automatic detection.
    # They remain available through explicit algorithm selection.
    AUTO_DETECT_EXCLUDED = {
        "rot13",
        "rot47",
        "rot5",
        "rot18",
        "caesar",
        "atbash",
        "vigenere",
        "rail_fence",
        "xor",
        "affine",
        "autokey",
        "beaufort",
        "gronsfeld",
        "porta",
        "columnar_transposition",
        "hill",
        "playfair",
        "scytale",
        "substitution",
    }

    @staticmethod
    def _normalize_algorithm(algorithm: str) -> str:
        return algorithm.lower().strip().replace("-", "_")

    @staticmethod
    def _has_required_parameters(
        name: str,
        kwargs: Dict[str, Any],
    ) -> bool:
        required = Decodify.REQUIRED_PARAMETERS.get(name, ())

        return all(
            parameter in kwargs and kwargs[parameter] is not None
            for parameter in required
        )

    @staticmethod
    def detect_algorithm(
        encoded: str,
        **kwargs: Any,
    ) -> Dict[str, float]:
        """
        Detect possible encoding algorithms.

        Ambiguous classical ciphers are excluded to prevent
        false-positive automatic detection.
        """
        raw = {}

        for name, (is_fn, _, _) in ALGORITHMS.items():

            if name in Decodify.AUTO_DETECT_EXCLUDED:
                raw[name] = 0.0
                continue

            if not Decodify._has_required_parameters(name, kwargs):
                raw[name] = 0.0
                continue

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
            return {
                name: score / total
                for name, score in weighted.items()
            }

        return {
            name: 0.0
            for name in weighted
        }

    @staticmethod
    def _call_decode(
        fn,
        name: str,
        encoded: str,
        kwargs: Dict[str, Any],
    ) -> str:
        """Call a decoder with its supported parameters."""

        if name == "caesar":
            return fn(encoded, shift=kwargs.get("shift", 3))

        if name == "vigenere":
            return fn(encoded, key=kwargs.get("key", "KEY"))

        if name == "rail_fence":
            return fn(encoded, rails=kwargs.get("rails", 3))

        if name == "xor":
            return fn(encoded, key=kwargs.get("key", "key"))

        if name == "affine":
            return fn(
                encoded,
                a=kwargs.get("a", 5),
                b=kwargs.get("b", 8),
            )

        if name in Decodify.REQUIRED_PARAMETERS:
            if not Decodify._has_required_parameters(name, kwargs):
                required = ", ".join(
                    Decodify.REQUIRED_PARAMETERS[name]
                )
                raise ValueError(
                    f"Algorithm '{name}' requires parameter(s): {required}"
                )

            parameters = {
                parameter: kwargs[parameter]
                for parameter in Decodify.REQUIRED_PARAMETERS[name]
            }

            return fn(encoded, **parameters)

        return fn(encoded)

    @staticmethod
    def _call_encode(
        fn,
        name: str,
        message: str,
        kwargs: Dict[str, Any],
    ) -> str:
        """Call an encoder with its supported parameters."""

        if name == "caesar":
            return fn(message, shift=kwargs.get("shift", 3))

        if name == "vigenere":
            return fn(message, key=kwargs.get("key", "KEY"))

        if name == "rail_fence":
            return fn(message, rails=kwargs.get("rails", 3))

        if name == "xor":
            return fn(message, key=kwargs.get("key", "key"))

        if name == "affine":
            return fn(
                message,
                a=kwargs.get("a", 5),
                b=kwargs.get("b", 8),
            )

        if name in Decodify.REQUIRED_PARAMETERS:
            if not Decodify._has_required_parameters(name, kwargs):
                required = ", ".join(
                    Decodify.REQUIRED_PARAMETERS[name]
                )
                raise ValueError(
                    f"Algorithm '{name}' requires parameter(s): {required}"
                )

            parameters = {
                parameter: kwargs[parameter]
                for parameter in Decodify.REQUIRED_PARAMETERS[name]
            }

            return fn(message, **parameters)

        return fn(message)

    @staticmethod
    def decode_message(
        encoded: str,
        algorithm: Optional[str] = None,
        **kwargs: Any,
    ) -> Tuple[str, Dict[str, float]]:
        """
        Decode using an explicit algorithm or automatic detection.

        Returns:
            Tuple[str, Dict[str, float]]:
                Decoded message and algorithm probabilities.
        """

        if not isinstance(encoded, str):
            return (
                "Decode error: Input must be a string.",
                {},
            )

        # Explicit algorithm selection.
        if algorithm:
            algorithm = Decodify._normalize_algorithm(algorithm)

            if algorithm not in ALGORITHMS:
                return (
                    f"Unsupported algorithm: {algorithm}",
                    {algorithm: 0.0},
                )

            _, decode_fn, _ = ALGORITHMS[algorithm]

            try:
                decoded = Decodify._call_decode(
                    decode_fn,
                    algorithm,
                    encoded,
                    kwargs,
                )

                return decoded, {algorithm: 1.0}

            except Exception as exc:
                return (
                    f"Decode error ({algorithm}): {exc}",
                    {algorithm: 1.0},
                )

        # Automatic detection.
        probabilities = Decodify.detect_algorithm(
            encoded,
            **kwargs,
        )

        candidates = sorted(
            probabilities.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        if not candidates or candidates[0][1] == 0.0:
            return (
                "Unable to decode the message. No known encoding detected.",
                probabilities,
            )

        # Try candidates in descending probability order.
        for name, probability in candidates:

            if probability <= 0.0:
                break

            _, decode_fn, _ = ALGORITHMS[name]

            try:
                decoded = Decodify._call_decode(
                    decode_fn,
                    name,
                    encoded,
                    kwargs,
                )

                # Mark the successfully selected algorithm.
                probabilities = {
                    algorithm_name: (
                        1.0 if algorithm_name == name else 0.0
                    )
                    for algorithm_name in probabilities
                }

                return decoded, probabilities

            except Exception:
                continue

        return (
            "Unable to decode the message. No matching decoder succeeded.",
            probabilities,
        )

    @staticmethod
    def encode_message(
        message: str,
        algorithm: str,
        **kwargs: Any,
    ) -> str:
        """Encode a message using the selected algorithm."""

        if not isinstance(message, str):
            return "Encode error: Message must be a string."

        algorithm = Decodify._normalize_algorithm(algorithm)

        if algorithm not in ALGORITHMS:
            return f"Unsupported algorithm: {algorithm}"

        _, _, encode_fn = ALGORITHMS[algorithm]

        try:
            return Decodify._call_encode(
                encode_fn,
                algorithm,
                message,
                kwargs,
            )

        except Exception as exc:
            return f"Encode error ({algorithm}): {exc}"

    @staticmethod
    def list_algorithms() -> list:
        """Return all registered algorithm names."""
        return sorted(ALGORITHMS.keys())


# Public convenience functions.

def decode_message(
    encoded: str,
    algorithm: Optional[str] = None,
    **kwargs: Any,
) -> Tuple[str, Dict[str, float]]:
    return Decodify.decode_message(
        encoded,
        algorithm=algorithm,
        **kwargs,
    )


def encode_message(
    message: str,
    algorithm: str,
    **kwargs: Any,
) -> str:
    return Decodify.encode_message(
        message,
        algorithm,
        **kwargs,
    )


def list_algorithms() -> list:
    return Decodify.list_algorithms()
