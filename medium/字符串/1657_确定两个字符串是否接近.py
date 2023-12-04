"""
https://leetcode.cn/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75
如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：

操作 1：交换任意两个 现有 字符。
例如，abcde -> aecdb
操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
你可以根据需要对任意一个字符串多次使用这两种操作。

给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。
"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 1.长度不一样，直接退出
        if len(word1) != len(word2):
            return False

        # 2.出现没有出现过的字符，退出
        a = [0 for i in range(26)]
        b = [0 for i in range(26)]
        for w1,w2 in zip(word1,word2):
            a[ord(w1) - ord('a')] += 1
            b[ord(w2) - ord('a')] += 1

        for i in range(26):
            if (a[i] == 0) != (b[i] == 0):
                return False

        # 3. 排序后不一致，代表无法转换
        a.sort()
        b.sort()
        for i in range(26):
            if a[i] != b[i]:
                return False

        return True

if __name__ == '__main__':
    print(Solution().closeStrings('abca', 'bcab'))