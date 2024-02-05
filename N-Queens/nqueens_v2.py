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
        hits = []
        nSlope = set()
        pSlope = set()

        def place(row, col):
            if (col in hits or (row - col) in pSlope or (row + col) in nSlope):
                return False
            return True

        def NQueens(N, row=0):
            for col in range(N):
                if (place(row, col)):
                    hits.append(col)
                    nSlope.add(row + col)
                    pSlope.add(row - col)
                    if (row == N - 1):
                        solutions.append([s[:c] + "Q" + s[c+1:] for c in hits])
                    else:
                        NQueens(N, row + 1)
                    hits.pop()
                    nSlope.remove(row + col)
                    pSlope.remove(row - col)

        NQueens(n)
        return solutions


if __name__ == '__main__':
    """test solveNque"""
    sol = Solution()
    print(sol.solveNQueens(4))
