# decodify/algorithms/brainfuck.py
def is_brainfuck(encoded: str) -> bool:
    """
    Check if string consists mainly of Brainfuck commands.
    """
    bf_chars = set("><+-.,[]")
    cleaned = "".join(c for c in encoded if not c.isspace())
    if not cleaned or len(cleaned) < 8:
        return False
    if not all(c in bf_chars for c in cleaned):
        return False
    # Distinctive if has pointer/loops, or is a long +/-/. program (encode style)
    if '>' in cleaned or '<' in cleaned or '[' in cleaned:
        return '.' in cleaned or '[' in cleaned
    # pure +/-/. : require many increments and at least one output, and no Morse-like short groups
    return cleaned.count('.') >= 1 and cleaned.count('+') + cleaned.count('-') >= 10 and ' ' not in encoded

def decode_brainfuck(encoded: str) -> str:
    """
    Interpret a Brainfuck program and return its output.
    Limited tape and steps for safety.
    """
    code = "".join(c for c in encoded if c in "><+-.,[]")
    tape = [0] * 30000
    ptr = 0
    pc = 0
    output = []
    steps = 0
    max_steps = 1000000
    jumps = {}
    stack = []
    for i, c in enumerate(code):
        if c == "[":
            stack.append(i)
        elif c == "]":
            if stack:
                start = stack.pop()
                jumps[start] = i
                jumps[i] = start
    while pc < len(code) and steps < max_steps:
        c = code[pc]
        if c == ">":
            ptr = (ptr + 1) % len(tape)
        elif c == "<":
            ptr = (ptr - 1) % len(tape)
        elif c == "+":
            tape[ptr] = (tape[ptr] + 1) % 256
        elif c == "-":
            tape[ptr] = (tape[ptr] - 1) % 256
        elif c == ".":
            output.append(chr(tape[ptr]))
        elif c == ",":
            pass
        elif c == "[":
            if tape[ptr] == 0:
                pc = jumps.get(pc, pc)
        elif c == "]":
            if tape[ptr] != 0:
                pc = jumps.get(pc, pc)
        pc += 1
        steps += 1
    return "".join(output)

def encode_brainfuck(message: str) -> str:
    """
    Generate a simple Brainfuck program that outputs the message.
    """
    code = []
    current = 0
    for ch in message:
        target = ord(ch)
        diff = target - current
        if diff > 0:
            code.append("+" * diff)
        elif diff < 0:
            code.append("-" * (-diff))
        code.append(".")
        current = target
    return "".join(code)
