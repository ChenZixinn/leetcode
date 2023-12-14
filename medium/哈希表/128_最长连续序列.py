"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_stack = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                current_stack = 1
                while num+1 in nums:
                    num += 1
                    current_stack += 1
                longest_stack = max(current_stack, longest_stack)
        return longest_stack


if __name__ == '__main__':
    res = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
    print(res)