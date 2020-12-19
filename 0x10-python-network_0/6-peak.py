#!/usr/bin/python3
"""Finds peak in unsorted list of integers"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers"""
    size = len(list_of_integers)
    if size < 3:
        return None
    peak = peak_finder(list_of_integers, 0, size - 1)
    return peak


def peak_finder(list_of_integers, left, rigth):
    """Find the peak in a list of unsorted list of integers"""
    mid = (rigth - left) // 2 + left
    integers = list_of_integers

    if mid + 1 >= rigth + 1 or integers[mid + 1] <= integers[mid]:
        if mid - 1 < 0 or integers[mid - 1] <= integers[mid]:
            return integers[mid]
        else:
            return find_peak(integers, 0, mid)
    else:
        return peak_finder(integers, mid + 1, rigth)
