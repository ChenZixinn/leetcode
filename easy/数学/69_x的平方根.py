"""
https://leetcode.cn/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150

给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分查找
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    res = Solution().mySqrt(4)
    print(res)