"""

"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_l = len(matrix)
        c_l = len(matrix[0])
        l = 0
        r = r_l * c_l - 1
        while l <= r:
            mid = (r - l) // 2 + l
            row = mid // c_l
            col = mid % c_l
            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':

    res = Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    print(res)
