"""

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。


"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table = {}
        for i, j in zip(s, t):
            hash_table[i] = hash_table.get(i, 0) + 1
            hash_table[j] = hash_table.get(j, 0) - 1
        for i in hash_table.values():
            if i<0:
                return False
        return True

if __name__ == '__main__':
    res = Solution().isAnagram('rac', 'car')
    print(res)