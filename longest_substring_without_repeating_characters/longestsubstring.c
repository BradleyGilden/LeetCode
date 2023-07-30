#include "string.h"
#include "stdio.h"

/**
 * lookback - checks for repetitions in sub array
 * @s: string with possible sub-strings
 * @start: start of substring
 * @current: current index, which is 1 index outside current substring
 * Return: 0 if there are repeated chars, 1 otherwise
 */
int lookback(int start, int current, char *s)
{
    for (int k = start; k < current; k++)
    {
        if (s[current] == s[k])
            return 0;
    }
    return 1;
}

/**
 * lengthOfLongestSubstring - Solution
 * @s: string with possible sub-strings
 * Return: length of sub-string
 */
int lengthOfLongestSubstring(char *s){
    int slen = strlen(s);
    int len = 0;
    int maxlen = 0;

    for (int i = 0; i < slen; i++)
    {
        for (int j = i; j < slen; j++)
        {
            // assuming i is the start index for every possible substring
            if (j == i)
            {
                len = 0;
                len++;
            }
            // do not match any letters from start index i to j (excluding)
            else if (lookback(i, j, s))
                len++;
            // check for max length every time a repeating character occurs
            else
            {
                maxlen = len > maxlen ? len : maxlen;
                len = 0;
                break;
            }
        }
        // check for max length after every iteration of a possible substring
        maxlen = len > maxlen ? len : maxlen;
    }

    return maxlen;
}

/**
 * main - Entry point
 * Return: 0 Always
 */
int main(void)
{
    printf("%d\n", lengthOfLongestSubstring("dvdf"));
    printf("%d\n", lengthOfLongestSubstring("abcabcbb"));
    printf("%d\n", lengthOfLongestSubstring("bbbbbb"));
    printf("%d\n", lengthOfLongestSubstring("pwwkew"));
    printf("%d\n", lengthOfLongestSubstring("abcd"));
    printf("%d\n", lengthOfLongestSubstring(""));
    printf("%d\n", lengthOfLongestSubstring("a"));
    printf("%d\n", lengthOfLongestSubstring("xyzaxyzzz"));

    return (0);
}
