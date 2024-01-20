#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 20-01-2024
"""
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    """finds longest common prefix"""
    length = len(strs[0])
    mincount = length
    for string in strs:
        comcount = 0
        ltemp = len(string)
        i = 0
        while i < ltemp and i < length:
            if (string[i] == strs[0][i]):
                comcount += 1
            else:
                break
            i += 1
        if (not comcount):
            return ""
        mincount = comcount if comcount < mincount else mincount
    return strs[0][:mincount]


if __name__ == '__main__':
    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["black", "blame", "blaring", "blade"]))
    print(longestCommonPrefix(["head", "heap", "dog"]))
