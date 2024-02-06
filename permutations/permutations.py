#!/usr/bin/env python3

"""
module contains a function that prints all permutations of a string

permutations("abc")
abc
acb
bac
bca
cba
cab
"""


def permutations(s: str):
    """create permutations of a string"""
    strlen = len(s)

    def permutate(s: str, used: set = set(), perm: list = []):
        if (len(used) == strlen):
            print(''.join(perm))
        for i in range(strlen):
            if (s[i] not in used):
                perm.append(s[i])
                used.add(s[i])
                permutate(s, used)
                perm.pop()
                used.remove(s[i])
    permutate(s)


if __name__ == '__main__':
    permutations("abcd")
