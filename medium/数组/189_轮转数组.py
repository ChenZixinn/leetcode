"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。



示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        new_num = [0] * n
        for i in range(n):
            new_num[(i+k)%n] = nums[i]
        for i in range(n):
            nums[i] = new_num[i]


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    Solution().rotate(nums, 3)
    print(nums)
