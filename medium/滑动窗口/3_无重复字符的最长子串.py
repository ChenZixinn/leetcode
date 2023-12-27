"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        lookup = set()
        n = len(s)
        cur_len = 0
        max_len = 0
        for i in range(n):
            cur_len +=1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = max(max_len,cur_len)
            lookup.add(s[i])
        return max_len


if __name__ == '__main__':
    # res = Solution().lengthOfLongestSubstring("abcabcbb")
    # print(res)
    # res = Solution().lengthOfLongestSubstring("bbbbbbb")
    # print(res)
    res = Solution().lengthOfLongestSubstring("pwwkew")
    print(res)
