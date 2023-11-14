"""
https://leetcode.cn/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import collections
        counter = collections.Counter(nums)
        return max(counter, key=counter.get)


if __name__ == '__main__':
    res = Solution().majorityElement([2, 2, 3, 3, 2, 3, 3])
    print(res)