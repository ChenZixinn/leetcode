"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符


示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
https://leetcode.cn/problems/edit-distance/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 初始化
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        print('*' * 20)
        # 测试打印
        for i in dp:
            print(i)
        print('*' * 20)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                n_pre = dp[i][j - 1] + 1
                m_pre = dp[i - 1][j] + 1
                left_down = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                dp[i][j] = min(left_down, n_pre, m_pre)

        return dp[-1][-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    res = Solution().minDistance(word1, word2)
    print(res)
