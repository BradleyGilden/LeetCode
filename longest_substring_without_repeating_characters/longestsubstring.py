"""                          Solution                           """


def lengthOfLongestSubstring(s: str) -> int:
    size = len(s)
    maxlen = 0
    length = 0

    for i in range(size):
        j = i
        while (j < size):
            # assuming i is the start index for every possible substring
            if j == i:
                length = 0
                length += 1
            # do not match any letters from start index i to j (excluding)
            elif s[j] not in s[i:j]:
                length += 1
            else:
                # check for max length every time a repeating character occurs
                maxlen = length if length > maxlen else maxlen
                length = 0
                break
            j += 1
        # check for max length after every iteration of a possible substring
        maxlen = length if length > maxlen else maxlen

    return maxlen


"""                   Test Solution                          """

if __name__ == '__main__':
    print(lengthOfLongestSubstring("dvdf"))
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring("abcd"))
    print(lengthOfLongestSubstring(""))
    print(lengthOfLongestSubstring("a"))
    print(lengthOfLongestSubstring("xyzaxyzzz"))
