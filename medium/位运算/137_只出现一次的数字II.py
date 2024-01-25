"""
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。



示例 1：

输入：nums = [2,2,3,2]
输出：3
示例 2：

输入：nums = [0,1,0,1,0,1,99]
输出：99
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((n >> i) & 1 for n in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans


if __name__ == '__main__':
    nums = [2,2,3,2]
    res = Solution().singleNumber(nums)
    print(res)