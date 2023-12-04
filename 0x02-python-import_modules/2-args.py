#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        print("{:d} argument".format(num_arguments), end="")
        if num_arguments > 1:
            print("s", end="")
        print(":")

        for i, arg in enumerate(arguments, start=1):
            print("{:d}: {:s}".format(i, arg))

