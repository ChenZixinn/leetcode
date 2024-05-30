"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左
子树
只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


示例 1：

输入：root = [2,1,3]
输出：true


示例 2：
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
"""
from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(root, lower=float("-inf"), upper=float("+inf")):
            if not root:
                return True
            val = root.val
            if val < lower or val > upper:
                return False
            if not is_valid(root.right, lower=val, upper=upper):
                return False
            if not is_valid(root.left, lower=lower, upper=val):
                return False
            return True
        return is_valid(root)


if __name__ == '__main__':
    root = TreeNode(5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6)))
    root2 = TreeNode(5, left=TreeNode(4), right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))
    root1 = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    res = Solution().isValidBST(root)
    print(res)
