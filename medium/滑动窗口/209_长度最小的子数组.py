"""
https://leetcode.cn/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        ans = n + 1
        total = 0
        while right < n:
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    res = Solution().minSubArrayLen(target, nums)
    print(res)
