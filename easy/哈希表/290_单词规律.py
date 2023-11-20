"""
https://leetcode.cn/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150

给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        p2w, w2p = {}, {}
        for p,w in zip(pattern, words):
            if (p in p2w and p2w[p] != w) or (w in w2p and w2p[w] != p):
                return False
            p2w[p] = w
            w2p[w] = p
        return True


if __name__ == '__main__':
    res = Solution().wordPattern("abba", "dog cat cat fish")
    print(res)