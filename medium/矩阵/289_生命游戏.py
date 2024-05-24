"""
根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        cp_board = [[col for col in row] for row in board]

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]
                    if (rows > r >= 0) and (cols > c >= 0) and cp_board[r][c] == 1:
                        live_neighbors += 1
                # 规则1/3
                if cp_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # 规则4
                if live_neighbors == 3:
                    board[row][col] = 1


if __name__ == '__main__':
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    # board = [[1]]
    Solution().gameOfLife(board)
    print(board)
