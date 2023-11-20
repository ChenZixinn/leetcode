"""
https://leetcode.cn/problems/palindrome-number/description/?envType=study-plan-v2&envId=top-interview-150

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 栈
        # stack = []
        # if x < 0:
        #     return False
        # if x < 10:
        #     return True
        # x = str(x)
        # n = len(x) // 2
        # # 入栈
        # for i in range(n):
        #     stack.append(x[i])
        # # 出栈
        # for i in range(len(x) - n, len(x)):
        #     if stack.pop() != x[i]:
        #         return False
        # return True

        # 官方解
        # 1、小于0的数不是回文数
        # 2、最后一位为0的数，只有x为0才是回文
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return reverted_number == x or reverted_number//10 == x


if __name__ == '__main__':
    # res = Solution().isPalindrome(-123)
    # print(res)
    res = Solution().isPalindrome(121)
    print(res)
    res = Solution().isPalindrome(11)
    print(res)
    res = Solution().isPalindrome(123)
    print(res)
    res = Solution().isPalindrome(9)
    print(res)
