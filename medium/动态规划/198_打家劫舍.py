"""
动态规划
https://leetcode.cn/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。


示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0

        # 分解成子问题
        """
        f(k) = 偷[0..k)房间的最大金额
        f(0) = 0
        f(1) = nums[0]
        f(k) = max { rob(k-1), rob(k-2) + nums[k-1]}
        """

        # n = len(nums)
        # dp = [0] * (n + 1)
        # dp[0] = 0
        # dp[1] = nums[0]
        pre = 0
        cur = 0
        # for i in range(2, n + 1):
        for i in nums:
            pre, cur = cur, max(cur,i+pre)
            # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return cur


if __name__ == '__main__':
    res = Solution().rob([1, 3, 4, 6])
    print(res)
