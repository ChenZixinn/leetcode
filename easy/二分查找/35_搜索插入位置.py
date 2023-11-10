"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(left, right):
            if left >= right:
                return left
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return search(left, mid-1)
            else:
                return search(mid + 1, right)

        n = len(nums)
        return search(0, n-1)


if __name__ == '__main__':
    res = Solution().searchInsert([1,3,5,6], 5)
    print(res)
    res = Solution().searchInsert([1,3,5,6], 2)
    print(res)
    res = Solution().searchInsert([1,3,5,6], 7)
    print(res)
