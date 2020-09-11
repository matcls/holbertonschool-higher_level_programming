#!/usr/bin/python3
def weight_average(my_list=[]):
    multup = 0
    sumtups = 0
    if my_list:
        for tup in my_list:
            multup += tup[0] * tup[1]
            sumtups += tup[1]
    else:
        return 0
    return multup / sumtups
