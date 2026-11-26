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

CHAR_TO_MORSE = {v: k for k, v in MORSE_CODE_DICT.items() if v != ' '}
CHAR_TO_MORSE[' '] = '/'

def is_morse(encoded: str) -> bool:
    """
    Check if the input is a valid Morse code encoded string.
    Requires only . - space / and at least one valid letter token.
    """
    cleaned = encoded.strip()
    if not cleaned:
        return False
    if not all(char in ".- /" for char in cleaned):
        return False
    # must contain at least one . or -
    if not ('.' in cleaned or '-' in cleaned):
        return False
    # try to parse at least one known token
    tokens = cleaned.replace('/', ' / ').split()
    known = sum(1 for t in tokens if t in MORSE_CODE_DICT)
    return known >= 1

def decode_morse(encoded: str) -> str:
    """
    Decode a Morse code encoded string.
    """
    # normalize multiple spaces
    text = " ".join(encoded.strip().split())
    words = text.split(" / ")
    decoded_message = []
    for word in words:
        letters = word.split()
        decoded_word = "".join([MORSE_CODE_DICT.get(letter, "") for letter in letters])
        decoded_message.append(decoded_word)
    return " ".join(decoded_message)

def encode_morse(message: str) -> str:
    """
    Encode a string to Morse code.
    """
    result = []
    for c in message.upper():
        if c in CHAR_TO_MORSE:
            result.append(CHAR_TO_MORSE[c])
        elif c == ' ':
            result.append('/')
    output = []
    current_word = []
    for p in result:
        if p == '/':
            if current_word:
                output.append(" ".join(current_word))
                current_word = []
            output.append("/")
        else:
            current_word.append(p)
    if current_word:
        output.append(" ".join(current_word))
    return " ".join(output)
