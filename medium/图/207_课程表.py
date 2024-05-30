"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。



示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

"""
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1、深度优先搜索
        # valid = True  # 记录是否合法
        # # result = list()  # 存放遍历结果
        # visited = [0] * numCourses  # 存放访问情况，0未访问，1正在访问，2访问过
        # edges = collections.defaultdict(list)  # 存放图
        # # 构建有向字典
        # for i in prerequisites:
        #     # i[1] 指向 i[0]
        #     edges[i[1]].append(i[0])
        #
        # def dfs(n: int):
        #     nonlocal valid
        #     visited[n] = 1  # 标记为当前访问
        #     for v in edges[n]:
        #         if visited[v] == 0:
        #             dfs(v)
        #             if not valid:
        #                 return
        #         elif visited[v] == 1:
        #             # 如果出现了正在访问的节点，代表出现了环
        #             valid = False
        #             return
        #     visited[n] = 2  # 标记为访问完成
        #     # result.append(n)
        #
        # # 遍历进行访问，访问过的数据跳过
        # for i in range(numCourses):
        #     if valid and visited[i] == 0:
        #         dfs(i)
        #
        # return valid

        # 2、广度优先搜索
        edges = collections.defaultdict(list)  # 存放图
        indeg = [0] * numCourses
        # 构建有向字典
        for i in prerequisites:
            # i[1] 指向 i[0]
            edges[i[1]].append(i[0])
            indeg[i[0]] += 1

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return visited == numCourses



if __name__ == '__main__':
    prerequisites = [[1, 0], [0, 1]]
    num_courses = 2
    res = Solution().canFinish(num_courses, prerequisites)
    print(res)

    prerequisites = [[1, 0]]
    num_courses = 2
    res = Solution().canFinish(num_courses, prerequisites)
    print(res)
