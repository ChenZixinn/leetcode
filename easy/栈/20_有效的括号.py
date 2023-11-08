"""

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # 加个?少点判断
        stack = ['?']
        char_dict = {'(': ')', '{': '}', '[': ']', '?':'?'}
        for i in s:
            if i in char_dict:
                stack.append(i)
            elif char_dict[stack.pop()] != i:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    res = Solution().isValid('()[]]{}')
    print(res)
