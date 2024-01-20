#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 20-01-2024
"""


def intToRoman(self, num: int) -> str:
    """converts integer to roman numeral"""
    inum = str(num)
    multiplier = 10 ** (len(inum) - 1)
    romanDict = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    


# if __name__ == '__main__':