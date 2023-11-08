"""
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/n-th-tribonacci-number
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        trib_list = [0,1,1]
        while len(trib_list) < n+1:
            trib_list.append(trib_list[-1] + trib_list[-2] + trib_list[-3])
        return trib_list[n]


if __name__ == '__main__':
    result = Solution().tribonacci(4)
    print(result)