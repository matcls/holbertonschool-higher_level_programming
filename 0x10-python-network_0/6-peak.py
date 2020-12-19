#!/usr/bin/python3
"""Finds peak in unsorted list of integers"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers
    """
    size = len(list_of_integers)
    if size < 3:
        return None
    else:
        integers = list_of_integers
        pivot = 0
        peak = integers[pivot]
        while pivot < len(integers):
            if pivot == 0 and pivot + 1 < len(integers)\
                and (integers[0] > integers[1]
                     or integers[0] == integers[1]):
                peak = integers[0]
            if pivot + 1 < len(integers)\
                and integers[pivot - 1] < integers[pivot]\
                    and integers[pivot] > integers[pivot + 1]:
                if integers[pivot] > peak:
                    peak = integers[pivot]
            pivot += 1
    return peak
