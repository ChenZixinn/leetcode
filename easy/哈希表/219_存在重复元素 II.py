"""
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for i, num in enumerate(nums):
            if num in hash_table and i - hash_table[num] <= k:
                return True
            hash_table[num] = i
        return False


if __name__ == '__main__':
    res = Solution().containsNearbyDuplicate([1, 0, 1, 1], 1)
    print(res)