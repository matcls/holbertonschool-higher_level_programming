#!/usr/bin/python3
"""Module for print a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of
    these characters: ., ? and :

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in [".", "?", ":"]:
        text = (i + "\n\n").join(
            [line.strip(" ¿") for line in text.split(i)])

    print(text, end="")
