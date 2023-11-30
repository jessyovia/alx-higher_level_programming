#!/usr/bin/python3
def fizzbuzz():
    for u in range(1, 101):
        if u % 3 == 0 and u % 5 == 0:
            print("FizzBuzz ", end="")
        elif u % 3 == 0:
            print("Fizz ", end="")
        elif u % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(u), end="")
