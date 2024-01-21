#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 21-01-2024
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """returns list of combinations of 3 ints that have a sum = 0"""
    length = len(nums)
    res = []
    for i in range(length):
        for j in range(length):
            if (i == j):
                continue
            for k in range(length):
                test = sorted([nums[i], nums[j], nums[k]])
                # filter out used combination
                if (k == i or k == j):
                    continue
                if (nums[i] + nums[j] + nums[k] == 0):
                    status = all(s != test for s in res)
                    if (res and status or not res):
                        res.append(test)
    return res


if __name__ == '__main__':
    print(threeSum([0,3,0,1,1,-1,-5,-5,3,-3,-3,0]))
