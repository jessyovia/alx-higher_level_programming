#!/usr/bin/python3
v = 0
for u in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(u - v)), end="")
    v = 32 if v == 0 else 0
