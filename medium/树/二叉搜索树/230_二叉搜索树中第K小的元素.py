"""
https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-interview-150
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

"""
from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


if __name__ == '__main__':
    r1 = TreeNode(1)
    r2 = TreeNode(2, r1)
    r4 = TreeNode(4)
    r6 = TreeNode(6)
    r3 = TreeNode(3, r2, r4)
    root = TreeNode(5, r3, r6)
    res = Solution().kthSmallest(root=root, k=6)
    print(res)
