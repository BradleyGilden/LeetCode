#!/usr/bin/env python3

"""
sum pairs implementation
"""


def sum_pair(nums, target):
    """ find a pair in nums that equate to the target
    """
    pairs = []
    numslen = len(nums)
    for i in range(numslen):
        for j in range(i + 1, numslen):
            if (nums[i] + nums[j] == target):
                pairs.append([nums[i], nums[j]])
    return pairs


if __name__ == '__main__':
    sp = sum_pair([3, 2, 4], 6)

    if sp:
        for pairs in sp:
            print(f"Pair found ({pairs[0]}, {pairs[1]})")
    else:
        print("Pair not found")

    sp = sum_pair([5, 2, 6, 8, 1, 9], 12)

    if sp:
        for pairs in sp:
            print(f"Pair found ({pairs[0]}, {pairs[1]})")
    else:
        print("Pair not found")
