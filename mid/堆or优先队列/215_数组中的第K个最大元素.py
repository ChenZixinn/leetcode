"""
堆
https://leetcode.cn/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=leetcode-75
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num<pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                return quick_select(small, k - len(nums) + len(small))
            return pivot
        return quick_select(nums, k)


if __name__ == '__main__':
    res = Solution().findKthLargest([5, 2, 9, 3, 7, 6], 5)
    print(res)

# nums = [5, 2, 9, 3, 7, 6]
# k = 5
# small = [2, 3]
# equal = [5]
# big = [9, 7, 6]