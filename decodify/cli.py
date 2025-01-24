# decodify/cli.py
import argparse
from decodify import decode_message

def main():
    parser = argparse.ArgumentParser(description="Decodify: A tool to detect and decode encoded messages.")
    parser.add_argument("input", nargs="?", help="The encoded message or file path.")
    parser.add_argument("-f", "--file", action="store_true", help="Read input from a file.")
    parser.add_argument("-o", "--output", help="Save the decoded message to a file.")
    parser.add_argument("-a", "--algorithm", help="Specify the decoding algorithm to use.")
    args = parser.parse_args()

    if not args.input:
        parser.print_help()
        return

    # Read input
    if args.file:
        try:
            with open(args.input, "r") as f:
                encoded = f.read().strip()
        except FileNotFoundError:
            print(f"Error: File '{args.input}' not found.")
            return
    else:
        encoded = args.input

    # Decode the message
    decoded, probabilities = decode_message(encoded, algorithm=args.algorithm)

    # Print results
    print(f"Decoded Message: {decoded}")
    print("Algorithm Probabilities:")
    for alg, prob in probabilities.items():
        print(f"  {alg}: {prob:.2f}")

    # Save output to file
    if args.output:
        try:
            with open(args.output, "w") as f:
                f.write(decoded)
            print(f"Decoded message saved to '{args.output}'.")
        except Exception as e:
            print(f"Error saving output: {e}")

if __name__ == "__main__":
    main()