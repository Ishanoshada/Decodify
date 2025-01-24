# decodify/algorithms/morse.py
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '/': ' '
}

def is_morse(encoded: str) -> bool:
    """
    Check if the input is a valid Morse code encoded string.
    """
    return all(char in [".", "-", " ", "/"] for char in encoded)

def decode_morse(encoded: str) -> str:
    """
    Decode a Morse code encoded string.
    """
    words = encoded.split(" / ")
    decoded_message = []
    for word in words:
        letters = word.split()
        decoded_word = "".join([MORSE_CODE_DICT.get(letter, "") for letter in letters])
        decoded_message.append(decoded_word)
    return " ".join(decoded_message)