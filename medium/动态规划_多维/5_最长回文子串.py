"""
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 0
        begin = 0
        # False表示不是回文字符串
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # L：回文长度
        for L in range(2, n + 1):
            # 遍历
            for i in range(n):
                j = i + L - 1
                if j >= n:
                    break

                # 判断是不是回文
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        # 长度小于3而且前后相同的是回文
                        dp[i][j] = True
                    else:
                        # 因为前后相同，所以判断里面的内容是不是回文即可
                        dp[i][j] = dp[i + 1][j - 1]
                # 记录最长的长度和begin下标
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin: begin + max_len]


if __name__ == '__main__':
    res = Solution().longestPalindrome("baba")
    print(res)