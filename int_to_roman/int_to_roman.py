#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 20-01-2024
"""


def intToRoman(num: int) -> str:
    """converts integer to roman numeral"""
    res = []
    inum = str(num)
    multiplier = len(inum) - 1
    romanDict = {
        '1000': 'M',
        '900': 'CM',
        '500': 'D',
        '400': 'CD',
        '100': 'C',
        '90': 'XC',
        '50': 'L',
        '40': 'XL',
        '10': 'X',
        '9': 'IX',
        '5': 'V',
        '4': 'IV',
        '1': 'I'
    }
    for n in inum:
        if n in romanDict:
            res.append(romanDict[n + ('0' * multiplier)])
        elif n > '5':
            res.append(romanDict['5' + ('0' * multiplier)])
            [res.append(romanDict['1' + ('0' * multiplier)]) for _ in range(int(n) - 5)]
        else:
            [res.append(romanDict['1' + ('0' * multiplier)]) for _ in range(int(n))]
        multiplier -= 1
    return ''.join(res)


if __name__ == '__main__':
    print(intToRoman(423))
