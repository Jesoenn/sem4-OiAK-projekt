import argparse
import sys

def positive_int(value):
    given_value = int(value)
    if given_value <= 0:
        raise argparse.ArgumentTypeError(f"{value} must be a positive integer")
    return given_value

# --help
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Montgomery multiplication algorithms. All numbers >0"
    )

    parser.add_argument("algorithm", type=int, choices=[0, 1],
                        help="0 - SOS, 1 - CIOS")
    parser.add_argument("words", type=positive_int, help="Words number")
    parser.add_argument("bits", type=positive_int, help="Bits per word")
    parser.add_argument("--file", type=str, default=None,
                        help="File to save output in")
    parser.add_argument("--a", type=positive_int, default=None,
                        help="Optional a to multiply")
    parser.add_argument("--b", type=positive_int, default=None,
                        help="Optional b to multiply")
    parser.add_argument("--n", type=positive_int, default=None,
                        help="n for modulo")
    parser.add_argument("--max_n", type=positive_int, default=None,
                        help="minimum n for modulo")
    parser.add_argument("--min_n", type=positive_int, default=None,
                        help="maximum n for modulo")

    args = parser.parse_args()
    # check if min_n > max_n
    if args.min_n is not None and args.max_n is not None:
        if args.min_n > args.max_n:
            print("ERROR: --min_n is bigger than --max_n.")
            sys.exit(1)

    return args