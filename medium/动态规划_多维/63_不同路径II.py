"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 以下两个循环先把第一行第一列走一遍，方便后面计算
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        # 从第一行第一列开始走，走过之后加上之前走过的次数，就得出了最终的路径条数
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] != 1:
                    dp[row][col] = dp[row - 1][col] + dp[row][col-1]
        return dp[m-1][n-1]


if __name__ == '__main__':
    Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])