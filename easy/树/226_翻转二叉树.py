"""
https://leetcode.cn/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
"""
from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == '__main__':
    r7 = TreeNode(9)
    r6 = TreeNode(6)
    r5 = TreeNode(3)
    r4 = TreeNode(1)
    r3 = TreeNode(7, r6, r7)
    r2 = TreeNode(2, r4, r5)
    r1 = TreeNode(4, r2, r3)
    Solution().invertTree(r1)
    print(r1)