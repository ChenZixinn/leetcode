"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # l = 0
        # u = 0
        # d = len(matrix)-1
        # r = len(matrix[0])-1
        # res = []
        # while True:
        #     # 按右、下、上、左的顺序执行
        #     for col in range(l, r+1):
        #         res.append(matrix[u][col])
        #     u += 1
        #     if u>d:break
        #     # 下
        #     for row in range(u, d+1):
        #         res.append(matrix[row][r])
        #     r-=1
        #     if r<l:break
        #     # 左
        #     for col in range(r, l-1, -1):
        #         res.append(matrix[d][col])
        #     d -= 1
        #     if d < u: break
        #     # 上
        #     for row in range(d, u-1, -1):
        #         res.append(matrix[row][l])
        #     l += 1
        #     if l>r:break
        # return res
        # res = []
        # while matrix:
        #     res += matrix.pop(0)
        #     matrix = [*zip(*matrix)][::-1]
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


if __name__ == '__main__':
    # res = Solution().spiralOrder(
    #     [[1, 2, 3, 4, 5],
    #      [6, 7, 8, 9, 10],
    #      [11, 12, 13, 14, 15],
    #      [16, 17, 18, 19, 20],
    #      [21, 22, 23, 24, 25]])
    res = Solution().spiralOrder(
        [[2,5,8],[4,0,-1]])
    print(res)
