#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 08-02-2024
"""


def permutations(sequence: list | tuple | str):
    """create permutations of a string"""
    llen = len(sequence)
    result = []
    seq = sequence
    if (type(sequence) is not list):
        seq = list(sequence)
    used = {seq[i]: 0 for i in range(llen)}
    for k in seq:
        used[k] += 1

    def permutate(seq: list, used: dict, perm: list = []):
        for i in range(llen):
            if (used[seq[i]] and perm + [seq[i]] not in result):
                perm.append(seq[i])
                used[seq[i]] -= 1
                if (all(v == 0 for v in used.values())):
                    result.append(perm.copy())
                else:
                    permutate(seq, used, perm)
                perm.pop()
                used[seq[i]] += 1
    permutate(seq, used)
    return result


if __name__ == '__main__':
    res = permutations(["a", "b", "b", "c"])
    for r in res:
        print(''.join(r))
