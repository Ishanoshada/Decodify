# decodify/cli.py
import argparse
from decodify import decode_message, encode_message, list_algorithms

def main():
    parser = argparse.ArgumentParser(
        description="Decodify: Detect and decode (or encode) messages with 25+ algorithms."
    )
    parser.add_argument("input", nargs="?", help="The encoded/plaintext message or file path.")
    parser.add_argument("-f", "--file", action="store_true", help="Read input from a file.")
    parser.add_argument("-o", "--output", help="Save the result to a file.")
    parser.add_argument("-a", "--algorithm", help="Specify the algorithm to use.")
    parser.add_argument("-e", "--encode", action="store_true", help="Encode instead of decode.")
    parser.add_argument("--key", help="Key for keyed ciphers (vigenere, xor, ...).")
    parser.add_argument("--shift", type=int, default=3, help="Shift for Caesar (default 3).")
    parser.add_argument("--rails", type=int, default=3, help="Rails for rail-fence (default 3).")
    parser.add_argument("--a", type=int, default=5, help="Affine 'a' coefficient.")
    parser.add_argument("--b", type=int, default=8, help="Affine 'b' coefficient.")
    parser.add_argument("-l", "--list", action="store_true", help="List supported algorithms.")
    args = parser.parse_args()

    if args.list:
        print("Supported algorithms:")
        for name in list_algorithms():
            print(f"  - {name}")
        return

    if not args.input:
        parser.print_help()
        return

    # Read input
    if args.file:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                text = f.read().strip()
        except FileNotFoundError:
            print(f"Error: File '{args.input}' not found.")
            return
        except Exception as e:
            print(f"Error reading file: {e}")
            return
    else:
        text = args.input

    kwargs = {}
    if args.key is not None:
        kwargs["key"] = args.key
    if args.shift is not None:
        kwargs["shift"] = args.shift
    if args.rails is not None:
        kwargs["rails"] = args.rails
    kwargs["a"] = args.a
    kwargs["b"] = args.b

    if args.encode:
        if not args.algorithm:
            print("Error: --algorithm is required when encoding.")
            return
        result = encode_message(text, args.algorithm, **kwargs)
        print(f"Encoded Message: {result}")
    else:
        decoded, probabilities = decode_message(text, algorithm=args.algorithm, **kwargs)
        print(f"Decoded Message: {decoded}")
        print("Algorithm Probabilities:")
        # show top ones
        sorted_probs = sorted(probabilities.items(), key=lambda x: -x[1])
        for alg, prob in sorted_probs:
            if prob > 0:
                print(f"  {alg}: {prob:.3f}")

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(result if args.encode else decoded)
            print(f"Result saved to '{args.output}'.")
        except Exception as e:
            print(f"Error saving output: {e}")

if __name__ == "__main__":
    main()
