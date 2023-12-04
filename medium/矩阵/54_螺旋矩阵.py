"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = 0
        col = 0
        rn = len(matrix) - 1
        rc = len(matrix[0]) - 1
        res = []
        # 按右、下、上、左的顺序执行
        while True:
            res.append(matrix[row][col])
            matrix[row][col] = -1
            if col < rn and matrix[row][col] != -1:
                col += 1
            elif row < rn:
                row += 1
            elif col >= 0:
                col -= 1
            else:
                row -=1
            if matrix[row][col] == -1:
                break
        return res


if __name__ == '__main__':
    res = Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(res)