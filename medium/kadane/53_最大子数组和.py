"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 0:
            return 0
        pre = 0
        res = nums[0]
        for i in range(n):
            pre = max(nums[i], pre + nums[i])
            res = max(res, pre)
        return res


if __name__ == '__main__':
    nums = [5,4,-1,7,8]
    res = Solution().maxSubArray(nums)
    print(res)