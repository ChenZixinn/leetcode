"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 问题化解为n//2进行四个方向的交替
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n+1) // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n - j - 1]
                matrix[n-i-1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp
        print(matrix)


if __name__ == '__main__':
    martrix = [[5,1,9,11],
               [2,4,8,10],
               [13,3,6,7],
               [15,14,12,16]]
    Solution().rotate(martrix)
    print(martrix == [[15, 13, 2, 5],
                      [14, 3, 4, 1],
                      [12, 6, 8, 9],
                      [16, 7, 10, 11]])