#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Extract command-line arguments excluding the script name
    arguments = sys.argv[1:]

    # Sum the integer values of the arguments
    total = sum(int(arg) for arg in arguments if arg.isdigit())

    print(total)
