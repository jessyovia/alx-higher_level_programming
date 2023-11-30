#!/usr/bin/python3
for u in range(97, 123):
    if (u == 101) or (u == 113):
        continue
    print(chr(u).format(), end="")
