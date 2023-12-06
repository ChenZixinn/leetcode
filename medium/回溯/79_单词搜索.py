"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, word, visited):
            if len(word) == 0:
                return True
            if 0 > row or row > rn or 0 > col or col > cn or visited[row][col]:
                return False
            if board[row][col] == word[0]:
                visited[row][col] = True
                # 递归附近的字母
                if (dfs(row - 1, col, word[1:], visited) or dfs(row, col - 1, word[1:], visited) or
                        dfs(row + 1, col, word[1:], visited) or dfs(row, col + 1, word[1:], visited)):
                    return True
            visited[row][col] = False
            return False

        rn = len(board) - 1
        cn = len(board[0]) - 1
        for r in range(len(board)):
            for c in range(len(board[0])):
                visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                if dfs(r, c, word, visited): return True
        return False


if __name__ == '__main__':
    res = Solution().exist(board=[["A", "B", "C", "E"],
                                  ["S", "F", "E", "S"],
                                  ["A", "D", "E", "E"]], word="ABCESEEEFS")
    print(res)
