"""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。



示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 用顺序相乘数组和逆序相乘数据
        # 除了n的乘积=L[n-1]*R[n+1]

        # length = len(nums)
        # L, R, answer = [0] * length, [0] * length, [0] * length
        # L[0] = 1
        # for i in range(length-1):
        #     L[i+1] = L[i] * nums[i]
        #
        # R[-1] = 1
        # for i in reversed(range(length-1)):
        #     R[i] = R[i+1] * nums[i+1]
        #
        # for i in range(length):
        #     answer[i] = L[i]*R[i]
        # return answer

        # 改进,空间复杂度O(1)
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(length-1):
            answer[i+1] = answer[i] * nums[i]
        R = 1
        for j in reversed(range(length-1)):
            R *= nums[j+1]
            answer[j] *= R
        return answer



if __name__ == '__main__':
    res = Solution().productExceptSelf([1,2,3,4])
    print(res)