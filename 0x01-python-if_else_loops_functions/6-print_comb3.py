#!/usr/bin/python3
for u in range(9):
    for v in range(u + 1, 10):
        if u * 10 + v < 89:
            print("{:d}{:d}".format(u, v), end=", ")
print("{:d}".format(89))
