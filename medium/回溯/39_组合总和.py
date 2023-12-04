"""
https://leetcode.cn/problems/combination-sum/description/?envType=study-plan-v2&envId=top-interview-150
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

对于给定的输入，保证和为 target 的不同组合数少于 150 个。



示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, size, path, target):
            """

            :param begin: 数组开始的下标
            :param size: 结束的下标
            :param path: 经过的路径
            :param target: 目标值
            :return:
            """
            # 命中时添加，超出时退出
            if target < 0:
                return
            if target == 0:
                res.append(path)
            # 从开始的下标到最后，遍历
            for index in range(begin, size):
                # 减掉当前值
                residue = target - candidates[index]
                # 排序后的数组，如果前面的数已经不符合，后面的数就无需再传
                if residue < 0:
                    break
                # 递归传入
                dfs(index, size, path + [candidates[index]], residue)

        size = len(candidates)
        res = []
        path = []
        candidates.sort()
        dfs(0, size, path, target)
        return res


if __name__ == '__main__':
    res = Solution().combinationSum([2, 3, 6, 7], 8)
    print(res)
