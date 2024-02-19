"""
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。

"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, t = len(s1), len(s2), len(s3)
        # 长度不匹配直接返回
        if n + m != t:
            return False
        # 定义数组
        f = [False for _ in range(m+1)]
        # 下标从1开始
        f[0] = True
        for i in range(n+1):
            for j in range(m+1):
                p = i + j - 1
                # 为True的条件：(1)当前字符与s3字符匹配;(2)上一个字符可以匹配
                if i > 0:
                    f[j] &= (s1[i - 1] == s3[p])
                if j > 0:
                    f[j] |= (s3[p] == s2[j - 1] and f[j - 1])
        return f[m]


if __name__ == '__main__':
    print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
