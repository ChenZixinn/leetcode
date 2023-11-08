"""
https://leetcode.cn/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。


"""


class Solution:
    def decodeString(self, s: str) -> str:
        # 存放(倍数, 临时字符串)
        stack = []
        res = ''
        mul = ''
        for i in s:
            # 遇到数字，保存到倍数临时变量mul中
            if i in '0123456789':
                mul += i
            # 左括号，先存储之前的结果，待会拼接到前面
            elif i == '[':
                stack.append((int(mul), res))
                mul = ''
                res = ''
            # 右括号，弹出倍数和前面的字符串，拼接结果
            elif i == ']':
                # m是倍数，r是之前的字符串
                m, r = stack.pop()
                # 把之前的字符串放到前面，然后把括号里的字符串乘以对应倍数
                res = r + (m * res)
            else:
                # 是字符，拼接到结果中
                res += i
        return res


if __name__ == '__main__':
    res = Solution().decodeString('5[x]abcd3[a2[cc]]abc')
    print(res)
