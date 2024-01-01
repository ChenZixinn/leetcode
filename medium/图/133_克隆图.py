"""
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node {
    public int val;
    public List<Node> neighbors;
}

"""

from common.graph import Node

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}

        def dfs(node: Optional['Node']):
            if node.val in visited:
                return visited[node.val]
            new_node = Node(node.val)
            visited[node.val] = new_node
            for i in node.neighbors:
                new_node.neighbors.append(dfs(i))
            return new_node

        return dfs(node)


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n3, n1]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    graph = Solution().cloneGraph(n1)
    print(graph)
