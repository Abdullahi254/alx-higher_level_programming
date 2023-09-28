#!/usr/bin/python3
"""
   this function finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    '''
        Finds the peak in a list of numbers
    '''
    if len(list_of_integers) > 0:
        peak = list_of_integers[0]
        for val in list_of_integers:
            if val > peak:
                peak =val
        return peak
    else:
        return None
