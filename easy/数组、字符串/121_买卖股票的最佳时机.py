"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = int(1e9)
        max_profit = 0
        for price in prices:
            min_price = min(price ,min_price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == '__main__':
    res = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print(res)