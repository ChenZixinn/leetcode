"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()
        r_n = len(matrix)
        c_n = len(matrix[0])
        for row in range(r_n):
            for col in range(c_n):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)
        for col in col_set:
            for row in range(r_n):
                matrix[row][col] = 0
        for row in row_set:
            for col in range(c_n):
                matrix[row][col] = 0



if __name__ == '__main__':
    res = [[0,1,2,0],
           [3,4,5,2],
           [1,3,1,5]]
    Solution().setZeroes(matrix=res)
    for i in res:
        print(i)
