"""
https://leetcode.cn/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150

给你一个二叉树的根节点 root ， 检查它是否轴对称。
"""
from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left: Optional[TreeNode], right: Optional[TreeNode]):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and check(left.left, right.right) and check(right.left, left.right)

        return check(root, root)


if __name__ == '__main__':
    r7 = TreeNode(1)
    r6 = TreeNode(3)
    r5 = TreeNode(3)
    r4 = TreeNode(1)
    r3 = TreeNode(2, r6, r7)
    r2 = TreeNode(2, r4, r5)
    r1 = TreeNode(4, r2, r3)
    res = Solution().isSymmetric(r1)
    print(res)