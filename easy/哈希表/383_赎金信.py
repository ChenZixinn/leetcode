"""
https://leetcode.cn/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。
"""
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 官方
        # if len(magazine) < len(ransomNote):
        #     return False
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)

        # 哈希表
        if len(magazine) < len(ransomNote):
            return False
        dict_ = {}
        for i in magazine:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        for i in ransomNote:
            if i not in dict_:
                return False
            else:
                if dict_[i] == 0:
                    return False
                else:
                    dict_[i] -= 1
        return True


if __name__ == '__main__':

    res = Solution().canConstruct("a", "b")
    print(res)