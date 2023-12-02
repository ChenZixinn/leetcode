"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

"""

from typing import List


class Solution:
    def inArea(self, grid, r, c):
        return r >= 0 and len(grid) > r and c >= 0 and len(grid[0]) > c

    def dfs(self, grid, r, c):
        if not self.inArea(grid, r, c):
            return
        # 0海洋，1陆地(未遍历)，2陆地(已遍历)
        if grid[r][c] != '1':
            return
        grid[r][c] = '2'
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        island_num = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    island_num += 1
                    self.dfs(grid, r, c)
        return island_num


if __name__ == '__main__':
    nums_list = [["1", "1", "1", "1", "0"],
                 ["1", "1", "0", "1", "0"],
                 ["1", "1", "0", "0", "0"],
                 ["0", "0", "0", "0", "0"]]
    res = Solution().numIslands(nums_list)
    print(res)