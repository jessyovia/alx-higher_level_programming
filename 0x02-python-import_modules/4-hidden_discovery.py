#!/usr/bin/python3

import sys

if __name__ == "__main__":
    n = len(sys.argv)
    
    if n == 1:
        print("0 arguments.")
    else:
        print(f"{n - 1} argument{'s' if n > 2 else ''}:")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"{i}: {arg}")
