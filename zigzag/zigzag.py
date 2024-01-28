def convert(s: str, numRows: int):
    """creates zig zag pattern from string"""
    size = len(s)
    if numRows == 1 or size <= numRows:
        return s
    zlist = []
    counter = 1
    increment = False
    tp = numRows
    for i in range(numRows):
        counter = 1
        increment = False
        if (i == numRows - 1):
            tp = numRows
        for j in range(i, size):
            # set the first turning point whenever counter is 1
            if (counter == 1):
                increment = not increment
            print(counter, s[j])
            # append when counter has reached 1
            if counter == 1:
                zlist.append(s[j])
            # set the second turning point at numrows, and continue to
            # decrease it by a factor of one, and reset at the start of the
            # last row
            if counter == tp:
                increment = not increment
            if increment:
                counter += 1
            else:
                counter -= 1
        tp -= 1
    return ''.join(zlist)


print(convert("PAYPALISHIRING", 4))
