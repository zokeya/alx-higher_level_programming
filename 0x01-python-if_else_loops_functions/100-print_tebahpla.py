#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{:s}".format(chr(i) if i % 2 == 0 else chr(1-32)), end="")
