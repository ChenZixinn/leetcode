"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]
"""
from copy import copy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def traceback(first):
            if first == n:
                ans.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                traceback(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        traceback(0)
        return ans


if __name__ == '__main__':
    res = Solution().permute([1, 2, 3,4])
    print(res)
