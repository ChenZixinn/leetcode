"""
https://leetcode.cn/problems/word-break/description/?envType=study-plan-v2&envId=top-interview-150

给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划
        # n = len(s)
        # dp = [False] * (n + 1)
        # dp[0] = True
        # for i in range(n):
        #     for j in range(1, n + 1):
        #         if dp[i] and s[i:j] in wordDict:
        #             dp[j] = True
        # return dp[-1]

        # 记忆化回溯
        import functools
        @functools.lru_cache()
        def back_track(s):
            if len(s) == 0:
                return True
            res = False
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    res = back_track(s[i:]) or res
            return res
        return back_track(s)

if __name__ == '__main__':
    word_dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    res = Solution().wordBreak(s, word_dict)
    print(res)