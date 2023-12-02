from typing import Optional, List

from common.data_structure import TreeNode


class Solution:
    """
    给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightmost_value_at_depth = dict()
        max_depth = -1

        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()
            if node is not None:
                max_depth = max(max_depth, depth)
                rightmost_value_at_depth.setdefault(depth, node.val)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]
