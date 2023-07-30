def convert(s: str, numRows: int) -> str:

    jumps = 2 * (numRows - 1) if numRows != 1 else numRows
    size = len(s)
    copy = s[:]
    idx = []
    i = 0
    j = 0
    k = 1
    print(jumps)
    while i < numRows:
        j = i
        while j < size and k < size:
            if (i == 0 and j == 0):
                j += jumps
                continue
            while (jumps == 1 and j < size and j in idx):
                j += 1
            slist = list(s)
            slist[k] = copy[j]
            s = "".join(slist)
            idx.append(j)
            k += 1
            j += jumps
        jumps //= 2
        i += 1

    return s


if __name__ == '__main__':
    print(convert("PAYPALISHIRING", 3))
    print(convert("PAYPALISHIRING", 4))
