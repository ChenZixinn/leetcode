from typing import Optional, List

from common.data_structure import TreeNode


class Solution:
    """
    给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = dict()
        max_depth = -1
        stack = [(root, 0)]
        while stack:
            root, depth = stack.pop()
            if root:
                max_depth = max(depth, max_depth)
                res.setdefault(depth, root.val)
                stack.append((root.left, depth+1))
                stack.append((root.right, depth+1))

        return [res[depth] for depth in range(max_depth + 1)]


if __name__ == '__main__':
    root = TreeNode(1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3, left=TreeNode(4)))
    res = Solution().rightSideView(root)
    print(res)
