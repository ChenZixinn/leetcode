"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            """
            回溯
            :param S: 当前括号列表
            :param left: 左括号数量
            :param right: 右括号数量
            :return:
            """
            # 如果括号数量已经符合要求，添加到答案中
            if len(S) == n*2:
                ans.append("".join(S))
            # 如果左括号没有超过括号组数量，继续添加
            if left < n:
                # 添加括号
                S.append('(')
                # 递归
                backtrack(S, left+1, right)
                # 删除刚添加的括号
                S.pop()
            # 如果右括号没有超过左括号，超过左括号则不合法
            if right < left:
                # 同上个if
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([],0, 0)
        return ans


if __name__ == '__main__':
    res = Solution().generateParenthesis(2)
    print(res)