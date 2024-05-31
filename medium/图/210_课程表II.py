"""
现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。



示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：[0,1]
解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
"""
import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        valid = True  # 记录是否合法
        result = list()  # 存放遍历结果
        visited = [0] * numCourses  # 存放访问情况，0未访问，1正在访问，2访问过
        edges = collections.defaultdict(list)  # 存放图
        # 构建有向字典
        for i in prerequisites:
            # i[1] 指向 i[0]
            edges[i[1]].append(i[0])

        def dfs(n: int):
            nonlocal valid
            visited[n] = 1  # 标记为当前访问
            for v in edges[n]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    # 如果出现了正在访问的节点，代表出现了环
                    valid = False
                    return
            visited[n] = 2  # 标记为访问完成
            result.append(n)

        # 遍历进行访问，访问过的数据跳过
        for i in range(numCourses):
            if valid and visited[i] == 0:
                dfs(i)
        if not valid:
            return list()

        return result[::-1]


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    res = Solution().findOrder(numCourses, prerequisites)
    print(res)

    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    res = Solution().findOrder(numCourses, prerequisites)
    print(res)