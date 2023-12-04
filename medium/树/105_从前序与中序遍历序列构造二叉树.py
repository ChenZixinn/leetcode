"""

给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

"""

from typing import List, Optional

from common.data_structure import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return

            # 先序遍历的第一个节点是根节点
            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_root]]
            # 数量
            num = inorder_root - inorder_left
            root = TreeNode(preorder[preorder_root])
            root.left = myBuildTree(preorder_root+1, preorder_left+num, inorder_left, inorder_root-1)
            root.right = myBuildTree(preorder_left + num + 1, preorder_right, inorder_root+1, inorder_right)
            return root

        n = len(inorder)
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n-1, 0, n-1)


if __name__ == '__main__':
    # [root, 先序遍历左节点， 先序遍历右节点]
    preorder = [3,9,20,15,7]
    # [中序遍历左节点， root， 中序遍历右节点]
    inorder = [9,3,15,20,7]
    root = Solution().buildTree(preorder, inorder)
    print(root)
