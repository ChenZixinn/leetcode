"""
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
"""
from typing import List


class Solution:
    def __init__(self):
        self.board = []
        self.cn = 0
        self.rn = 0

    def dfs(self, row, col):
        if not 0 <= row < self.rn or not 0 <= col < self.cn or self.board[row][col] != 'O':
            return
        self.board[row][col] = 'A'
        self.dfs(row - 1, col)
        self.dfs(row + 1, col)
        self.dfs(row, col + 1)
        self.dfs(row, col - 1)

    def solve(self, board: List[List[str]]) -> None:
        self.board = board
        self.rn = len(board)
        self.cn = len(board[0])
        if self.rn <= 2 or self.cn <= 2:
            return

        for i in range(self.rn):
            self.dfs(i, 0)
            self.dfs(i, self.cn - 1)
        for j in range(self.cn):
            self.dfs(0, j)
            self.dfs(self.rn - 1, j)

        for row in range(self.rn):
            for col in range(self.cn):
                if board[row][col] == 'A':
                    self.board[row][col] = 'O'
                elif board[row][col] == 'O':
                    self.board[row][col] = 'X'


if __name__ == '__main__':
    res = [["X", "X", "X", "X"],
           ["X", "O", "O", "X"],
           ["X", "X", "O", "X"],
           ["X", "O", "X", "X"]]
    res = [["O", "O", "O"],
           ["O", "O", "O"],
           ["O", "O", "O"]]
    res = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Solution().solve(res)
    print(res)
