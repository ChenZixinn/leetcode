"""
动态规划
https://leetcode.cn/problems/unique-paths/description/?envType=study-plan-v2&envId=leetcode-75
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

"""


# class Solution:
#     def unique_path_(self, i, j, x):
#         if i == len(x[0]) - 1 and j == len(x) - 1:
#             return 1
#         # 往右走
#         res = 0
#         if i < len(x[0]) - 1:
#             res += self.unique_path_(i + 1, j, x)
#         # 往下走
#         if j < len(x) - 1:
#             res += self.unique_path_(i, j + 1, x)
#         return res
#
#     def uniquePaths(self, m: int, n: int) -> int:
#
#         x = [[0] * n for _ in range(m)]
#         return self.unique_path_(0, 0, x)

# 官方答案
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]

        return cur[-1]


if __name__ == '__main__':
    res = Solution().uniquePaths(23, 12)
    print(res)
