"""
https://leetcode.cn/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 时间O(|s|)  空间O(|s|)
        # sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        # n = len(sgood)
        # left, right = 0, n-1
        # while left < right:
        #     if sgood[left] != sgood[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        # 空间O(1)
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            while left < n and not s[left].isalnum():
                left += 1
            while right > 0 and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True


if __name__ == '__main__':
    res = Solution().isPalindrome('A man, a plan, a canal: Panama')
    print(res)
