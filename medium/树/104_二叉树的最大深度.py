"""
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
"""
from typing import Optional

from common.data_structure import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def deep_search(root: Optional[TreeNode], deep):
            if not root:
                return deep
            deep += 1
            return max(deep_search(root.left, deep), deep_search(root.right, deep))
        return deep_search(root, 0)


if __name__ == '__main__':
    root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    depth = Solution().maxDepth(root)
    print(depth)
