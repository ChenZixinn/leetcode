"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1
"""
from common.data_structure import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def dfs(root):
            if not root:
                return False
            nonlocal ans
            f_lson = dfs(root.left)
            f_rson = dfs(root.right)
            if (f_rson and f_lson) or ((root == p or root == q) and (f_rson or f_lson)):
                ans = root
            return f_rson or f_lson or (root == p or root == q)
        dfs(root)
        return ans


if __name__ == '__main__':
    p = TreeNode(9)
    q = TreeNode(11)
    root = TreeNode(3,left=TreeNode(2, left=TreeNode(4, left=TreeNode(8), right=p), right=TreeNode(5, left=TreeNode(10), right=q)))
    ancestor = Solution().lowestCommonAncestor(root, p , q)
    print(ancestor)
