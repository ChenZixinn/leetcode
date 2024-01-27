"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_pos, end, step = 0, 0, 0  # 当前能跳到的最远位置，当前右边界，已跳的步数
        for i in range(n - 1):
            if max_pos >= i:  # 确保当前位置是能到达的位置
                max_pos = max(max_pos, i + nums[i])  # 求出最远能到达的位置
                if i == end:  # 达到右边界
                    end = max_pos  # 重新设置右边界
                    step += 1  # 步数+1
        return step


if __name__ == '__main__':
    res = Solution().jump([2, 3, 1, 1, 4])
    print(res)
