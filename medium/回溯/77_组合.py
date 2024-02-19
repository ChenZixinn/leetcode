"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

示例 1：

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp: List = []
        res: List[List] = []

        def dfs(cur, n, k):
            # 长度不够时，退出
            if (len(temp) + (n - cur + 1) < k):
                return
            # 长度够时，添加到结果
            if len(temp) == k:
                res.append(temp.copy())
                return
            # 考虑当前位置
            temp.append(cur)
            dfs(cur + 1, n, k)
            # 不考虑当前位置
            temp.pop()
            dfs(cur + 1, n, k)


        dfs(1, n, k)
        return res


if __name__ == '__main__':
    print(Solution().combine(1, 1))
