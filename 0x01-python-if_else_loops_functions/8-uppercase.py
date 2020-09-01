#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            dif = 32
        else:
            dif = 0
        print("{:c}".format(ord(letter) - dif), end="")
    print()
