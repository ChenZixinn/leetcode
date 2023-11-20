"""
https://leetcode.cn/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 哈希表，存储相应位置中对应的另一个字符
        s2t, t2s = {}, {}
        for a, b in zip(s, t):
            if (b in t2s and t2s[b] != a) or (a in s2t and s2t[a] != b):
                return False
            t2s[b] = a
            s2t[a] = b
        return True


if __name__ == '__main__':
    res = Solution().isIsomorphic('egg', 'add')
    print(res)
    res = Solution().isIsomorphic('bbbaaaba', 'aaabbbba')
    print(res)
