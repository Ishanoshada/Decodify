# decodify/decodify.py
from typing import Dict, Tuple
from .algorithms import (
    is_base64, decode_base64,
    is_hex, decode_hex,
    is_url_encoded, decode_url,
    is_binary, decode_binary,
    is_morse, decode_morse,
)

class Decodify:
    @staticmethod
    def detect_algorithm(encoded: str) -> Dict[str, float]:
        """
        Detect the likelihood of each encoding algorithm being used.
        """
        detection_results = {
            "base64": is_base64(encoded),
            "hex": is_hex(encoded),
            "url": is_url_encoded(encoded),
            "binary": is_binary(encoded),
            "morse": is_morse(encoded),
        }

        # Normalize probabilities to sum to 1
        total = sum(detection_results.values())
        if total > 0:
            for key in detection_results:
                detection_results[key] /= total
        else:
            # If no algorithm is detected, set all probabilities to 0
            for key in detection_results:
                detection_results[key] = 0.0

        return detection_results

    @staticmethod
    def decode_message(encoded: str, algorithm: str = None) -> Tuple[str, Dict[str, float]]:
        """
        Decode the message using the specified algorithm or by detecting the most likely one.
        """
        if algorithm:
            # Use the specified algorithm
            if algorithm == "base64":
                decoded = decode_base64(encoded)
            elif algorithm == "hex":
                decoded = decode_hex(encoded)
            elif algorithm == "url":
                decoded = decode_url(encoded)
            elif algorithm == "binary":
                decoded = decode_binary(encoded)
            elif algorithm == "morse":
                decoded = decode_morse(encoded)
            else:
                decoded = "Unsupported algorithm."
            return decoded, {algorithm: 1.0}
        else:
            # Detect the algorithm
            algorithm_probabilities = Decodify.detect_algorithm(encoded)
            most_likely_algorithm = max(algorithm_probabilities, key=algorithm_probabilities.get)

            if algorithm_probabilities[most_likely_algorithm] == 0.0:
                return "Unable to decode the message.", algorithm_probabilities

            if most_likely_algorithm == "base64":
                decoded = decode_base64(encoded)
            elif most_likely_algorithm == "hex":
                decoded = decode_hex(encoded)
            elif most_likely_algorithm == "url":
                decoded = decode_url(encoded)
            elif most_likely_algorithm == "binary":
                decoded = decode_binary(encoded)
            elif most_likely_algorithm == "morse":
                decoded = decode_morse(encoded)
            else:
                decoded = "Unable to decode the message."

            return decoded, algorithm_probabilities