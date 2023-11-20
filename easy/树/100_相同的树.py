"""


给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

"""
from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    c1 = TreeNode(2)
    r1 = TreeNode(1, c1, None)

    c2 = TreeNode(2)
    r2 = TreeNode(1,  c2)
    res = Solution().isSameTree(r1, r2)
    print(res)