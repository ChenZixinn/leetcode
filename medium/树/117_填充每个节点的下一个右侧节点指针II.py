"""
给定一个二叉树：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。

初始状态下，所有 next 指针都被设置为 NULL 。
"""
from queue import Queue

from common.data_structure import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        from queue import Queue
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            n = queue.qsize()
            pre = None
            for _ in range(n):
                cur: Node = queue.get()
                if pre:
                    pre.next = cur
                pre = cur
                if cur.left:
                    queue.put(cur.left)
                if cur.right:
                    queue.put(cur.right)
        return root


if __name__ == '__main__':
    r7 = Node(7)
    r5 = Node(5)
    r4= Node(4)
    r2 = Node(2, r4, r5)
    r3 = Node(3, right=r7)
    root = Node(1, r2, r3)
    Solution().connect(root=root)
    print(root)

