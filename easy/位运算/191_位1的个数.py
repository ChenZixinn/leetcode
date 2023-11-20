"""
https://leetcode.cn/problems/number-of-1-bits/description/?envType=study-plan-v2&envId=top-interview-150

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n & 1 == 1:
                res+=1
            n >>= 1

        return res

if __name__ == '__main__':
    res = Solution().hammingWeight(0b00000000000000000000000000001011)
    print(res)
    res = Solution().hammingWeight(0b00000000000000000000000010000000)
    print(res)
    res = Solution().hammingWeight(0b11111111111111111111111111111101)
    print(res)