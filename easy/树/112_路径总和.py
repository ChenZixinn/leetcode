"""
https://leetcode.cn/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150

给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。
"""
from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


if __name__ == '__main__':
    # r10 = TreeNode(1)
    # r9 = TreeNode(2)
    # r8 = TreeNode(7)
    # r7 = TreeNode(4, right=r10)
    # r6 = TreeNode(13)
    # r4 = TreeNode(11, r8, r9)
    # r3 = TreeNode(8, r6, r7)
    # r2 = TreeNode(4, r4)
    # r1 = TreeNode(5, r2, r3)
    # res = Solution().hasPathSum(r1, 22)
    # print(res)
    r2 = TreeNode(2)
    r1 = TreeNode(1, r2)
    res = Solution().hasPathSum(r1, 1)
    print(res)
