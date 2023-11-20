"""
https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150

给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

差值是一个正数，其数值等于两值之差的绝对值。
"""
import sys
from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def __init__(self):
        self.ans = sys.maxsize
        self.pre = -1

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return

        self.dfs(root.left)
        if self.pre == -1:
            self.pre = root.val
        else:
            self.ans = min(root.val - self.pre, self.ans)
            self.pre = root.val

        self.dfs(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans


if __name__ == '__main__':
    r4 = TreeNode(1)
    r5 = TreeNode(3)
    r2 = TreeNode(2, r4, r5)
    r3 = TreeNode(6)
    r1 = TreeNode(4, r2, r3)
    res = Solution().getMinimumDifference(r1)
    print(res)