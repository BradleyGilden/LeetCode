#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 05-02-2024
"""


class Solution:
    def solveNQueens(self, n: int):
        """
        find all possible orientations of N number of queens on an NxN chess
        board
        """
        solutions = []
        s = "." * n

        def place(row, col, hits):
            for r, c in enumerate(hits):
                if (c == col or row - col == r - c or row + col == r + c):
                    return False
            return True

        def NQueens(N, row=0, hits=[]):
            for col in range(N):
                if (place(row, col, hits)):
                    hits.append(col)
                    if (row == N - 1):
                        solutions.append([s[:c] + "Q" + s[c+1:] for c in hits])
                    else:
                        NQueens(N, row + 1, hits)
                    hits.pop()

        NQueens(n)
        return solutions


if __name__ == '__main__':
    """test solveNque"""
    sol = Solution()
    print(sol.solveNQueens(5))
