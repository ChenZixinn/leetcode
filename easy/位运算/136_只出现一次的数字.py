"""
https://leetcode.cn/problems/single-number/description/?envType=study-plan-v2&envId=top-interview-150

给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
"""
from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 异或：如[4, 2, 2] 1000 ^ 0010 = 1010, 1010 ^ 0010 = 1000
        # ans = nums[0]
        # for i in nums[1:]:
        #     ans ^= i
        # return ans

        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    res = Solution().singleNumber([2, 2, 1])
    print(res)
    res = Solution().singleNumber([4,1,2,1,2])
    print(res)
    res = Solution().singleNumber([1])
    print(res)