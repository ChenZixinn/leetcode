"""

给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
"""
from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + 1 + self.countNodes(root.right)


if __name__ == '__main__':
    r6 = TreeNode(6)
    r5 = TreeNode(5)
    r4 = TreeNode(4)
    r3 = TreeNode(3, r6)
    r2 = TreeNode(2, r4, r5)
    r1 = TreeNode(1, r2, r3)
    res = Solution().countNodes(r1)
    print(res)