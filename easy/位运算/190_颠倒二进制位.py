"""
https://leetcode.cn/problems/reverse-bits/description/?envType=study-plan-v2&envId=top-interview-150

颠倒给定的 32 位无符号整数的二进制位。
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        # 异或
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1

        return res

if __name__ == '__main__':
    n = 964176192
    # 输出n的二进制
    print(bin(n))
    res = Solution().reverseBits(n)
    print(res)