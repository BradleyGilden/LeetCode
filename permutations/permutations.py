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
    used = set()
    strlen = len(s)
    perm = []
    def permutate(s: str, used: set):
        for i in range(strlen):
            if (s[i] not in used):
                perm.append(s[i])
                used.add(s[i])
                if (len(used) == strlen):
                    print(''.join(perm))
                else:
                    permutate(s, used)
            perm.pop()
            used.remove(s[i])
    permutate(s, used)


if __name__ == '__main__':
    permutations("abc")
