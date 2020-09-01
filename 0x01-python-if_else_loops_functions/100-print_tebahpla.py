#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        dif = 0
    else:
        dif = 32
    print("{:c}".format(letter - dif), end="")
