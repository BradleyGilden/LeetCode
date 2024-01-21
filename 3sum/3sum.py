#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 21-01-2024
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """returns list of combinations of 3 ints that have a sum = 0"""
    nums.sort()
    length = len(nums)
    res = []

    for i in range(length - 2):
        # Skip duplicate elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, length - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])

                # Skip duplicate elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return res


if __name__ == '__main__':
    print(threeSum([0,3,0,1,1,-1,-5,-5,3,-3,-3,0]))
