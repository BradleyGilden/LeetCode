#!/usr/bin/env python3

"""
implements a function to shift 0's to end of array
"""

def shift_zeros(arr):
    """ shifts zero's to end of array
    """
    arrlen = len(arr)
    j = arrlen - 1
    for i in range(arrlen - 1):
        if (i >= j):
            break
        if (arr[i] == 0):
            while (j > 0 and arr[j] == 0):
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    print(arr)
    shift_zeros(arr)
    print(arr)
    arr = [23, 0, 12, 0, 0, 0, 12, 23, 0, 1, 0]
    print(arr)
    shift_zeros(arr)
    print(arr)
