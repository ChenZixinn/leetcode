"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。



示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找
        n = len(nums)
        l = 0
        r = n - 1
        idx = -1

        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                idx = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if idx == -1:
            return [-1, -1]
        res = [idx, idx]
        while res[0]-1 >= 0 and nums[res[0] - 1] == nums[idx]:
            res[0] -= 1

        while res[1]+1 < n and nums[res[1] + 1] == nums[idx]:
            res[1] += 1
        return res



if __name__ == '__main__':
    print(Solution().searchRange(nums=[1,1,2], target=1))
    # print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
    # print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6))
    # print(Solution().searchRange(nums = [], target = 0))