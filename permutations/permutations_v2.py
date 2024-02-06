#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 06-02-2024
"""


def permutations(nums):
    """create permutations of a string"""
    llen = len(nums)
    result = []

    def permutate(nums: list, used: set = set(), perm: list = []):
        for i in range(llen):
            if (nums[i] not in used):
                perm.append(nums[i])
                used.add(nums[i])
                if (len(used) == llen):
                    print(perm)
                    result.append(perm.copy())
                else:
                    permutate(nums, used)
                perm.pop()
                used.remove(nums[i])
    permutate(nums)
    return result


if __name__ == '__main__':
    print(permutations([1, 2, 3]))
