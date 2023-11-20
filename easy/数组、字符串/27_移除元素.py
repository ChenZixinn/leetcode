"""
https://leetcode.cn/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != val:
                if left != right:
                    nums[left] = nums[right]
                else:
                    print(1)
                left += 1
            right += 1
        return left


if __name__ == '__main__':
    nums = [3,2,2,3]
    res = Solution().removeElement(nums, 3)
    print(nums)
    print(res)
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    res = Solution().removeElement(nums, 2)
    print(nums)
    print(res)