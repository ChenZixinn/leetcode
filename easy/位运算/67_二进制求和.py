"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        carry = 0
        ans = []
        for i in range(n):
            carry += int(a[len(a)-1-i]) if i < len(a) else 0
            carry += int(b[len(b)-1-i]) if i < len(b) else 0
            ans.append(str(carry % 2))
            carry //= 2
        if carry:
            ans.append('1')
        ans.reverse()
        return "".join(ans)


if __name__ == '__main__':
    res = Solution().addBinary('1010', '1011')
    print(res)
