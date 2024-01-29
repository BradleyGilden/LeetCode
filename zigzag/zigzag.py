"""
solution using peaks and relative peaks
"""


def convert(s: str, numRows: int):
    """creates zig zag pattern from string"""
    size = len(s)
    if numRows == 1 or size <= numRows:
        return s
    zlist = []
    counter = 1
    peak = 2 * numRows - 1  # 2n -1

    for i in range(numRows):
        counter = i + 1 if i != numRows - 1 else 1
        rpeak = 1 + i  # related peak
        for j in range(i, size):
            if (i == 0 or i == numRows - 1):
                if (counter == peak or counter == 1):
                    zlist.append(s[j])
                    counter = 1
            else:
                if (j == i or counter == rpeak):
                    zlist.append(s[j])
                    # changed to the new relative peak once met
                    rpeak = peak - i if rpeak == 1 + i else 1 + i
                if (counter == peak):
                    counter = 1
            counter += 1

    return ''.join(zlist)


print(convert("PAYPALISHIRING", 6))
