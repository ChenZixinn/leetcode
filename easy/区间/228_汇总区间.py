"""
https://leetcode.cn/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150
给定一个  无重复元素 的 有序 整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def f(i, j) -> str:
            return str(nums[i]) if i==j else f'{nums[i]}->{nums[j]}'
        i = 0
        n = len(nums)
        res = []
        while i < n:
            j = i
            while j < n - 1 and nums[j + 1] == nums[j] + 1:
                j += 1
            res.append(f(i, j))
            i = j + 1

        return res

if __name__ == '__main__':
    res = Solution().summaryRanges([0,2,3,4,6,8,9])
    print(res)