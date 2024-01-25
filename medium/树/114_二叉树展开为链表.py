"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。

"""
from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stack = [root]
        pre = None
        while stack:
            cur = stack.pop()
            if pre:
                pre.right = cur
                pre.left = None
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            pre = cur





if __name__ == '__main__':
    r4 = TreeNode(4)
    r6 = TreeNode(6)
    r5 = TreeNode(5, r6)
    r3 = TreeNode(3)
    r2 = TreeNode(2, r3,r4)
    r1 = TreeNode(1, r2, r5)
    Solution().flatten(r1)
    print(r1)