# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # def dfs(root: Optional[TreeNode], num):
        #     num = num * 10 + root.val
        #
        #     if not root.left and not root.right:
        #         nonlocal count
        #         count += num
        #         return
        #
        #     if root.left:
        #         dfs(root.left, num)
        #     if root.right:
        #         dfs(root.right, num)
        #
        # count = 0
        # dfs(root, 0)
        # return count

        # 官方
        def dfs(root:Optional[TreeNode], pre_total:int):
            if not root:
                return 0
            total = pre_total *  10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)
        return dfs(root, 0)


if __name__ == '__main__':

    # r5 = TreeNode(1)
    # r4 = TreeNode(5)
    # r2 = TreeNode(9, r4, r5)
    # r3 = TreeNode(0)
    # root = TreeNode(4, r2,r3)
    r3 = TreeNode(3)
    r2 = TreeNode(2)
    r1 = TreeNode(1, r2, r3)
    res = Solution().sumNumbers(r1)
    print(res)