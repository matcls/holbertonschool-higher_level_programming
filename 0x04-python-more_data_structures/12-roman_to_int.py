#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if (roman_string) and (isinstance(roman_string, str)):
        for i in range(len(roman_string)):
            if i + 1 >= len(roman_string):
                num += roman[roman_string[i]]
                break
            if roman[roman_string[i]] < roman[roman_string[i + 1]]:
                num -= roman[roman_string[i]]
            else:
                num += roman[roman_string[i]]
        return num
    return 0
