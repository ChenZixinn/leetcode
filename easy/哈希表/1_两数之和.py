"""
https://leetcode.cn/problems/two-sum/?envType=study-plan-v2&envId=top-100-liked

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if (target - num) in hash_table:
                return [hash_table[(target - num)], i]
            hash_table[num] = i


if __name__ == '__main__':
    res = Solution().twoSum([1, 3, 2], 5)
    print(res)