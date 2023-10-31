"""
https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75

n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。

路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。

今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。

请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。

题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 。
"""
from collections import deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 构建无向图
        graph = []
        for i in range(n):
            graph.append([])
        for u, v in connections:
            # 1 代表顺向  0 代表逆向
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        print(graph)
        # BFS
        res = 0
        queue = deque()
        queue.append(0)
        # 记录是否访问过
        visited = [False] * n
        visited[0] = True
        while len(queue) > 0:
            x = queue.popleft()
            for y, w in graph[x]:
                if visited[y]:
                    continue
                visited[y] = True
                res += w
                # 广度优先遍历
                queue.append(y)

        return res


if __name__ == '__main__':
    print(Solution().minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
