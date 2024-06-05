"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
子序列
。
示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = []
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    # res = Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    # print(res)
    # res = Solution().lengthOfLIS([0,1,0,3,2,3])
    # print(res)
    # res = Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7])
    # print(res)
    res = Solution().lengthOfLIS([4, 10, 4, 3, 8, 9])  # 预期结果3
    print(res)
