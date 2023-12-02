from typing import Optional, List

from common.data_structure import TreeNode


class Solution:
    """
    hash表+递归实现
    # [中序遍历左节点， root, 中序遍历右节点]
    inorder = [9, 3, 15, 20, 7]
    # [后序遍历左节点，后序遍历右节点, root]
    postorder = [9, 15, 7, 20, 3]
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def my_build_tree(inorder_left, inorder_right, postorder_left, postorder_right):
            if postorder_left > postorder_right:
                return
            # 后序遍历的最后一个元素是根节点
            post_root_index = postorder_right
            # 根据根节点得到中序遍历中根节点的位置
            inorder_root_index = index[postorder[post_root_index]]
            # 构建根节点
            root = TreeNode(postorder[post_root_index])
            # 左节点的数量
            num = inorder_root_index - inorder_left
            # [中序遍历左节点， root, 中序遍历右节点]
            root.left = my_build_tree(inorder_left, inorder_left + num-1, postorder_left, postorder_left+num-1)
            # [后序遍历左节点，后序遍历右节点, root]
            root.right = my_build_tree(inorder_root_index + 1, inorder_right, postorder_left+num, postorder_right - 1)
            return root

        # 构建hashtable
        index = {element: i for i, element in enumerate(inorder)}
        return my_build_tree(0, len(inorder) - 1, 0, len(postorder) - 1)


if __name__ == '__main__':
    # [中序遍历左节点， root, 中序遍历右节点]
    inorder = [9, 3, 15, 20, 7]
    # [后序遍历左节点，后序遍历右节点, root]
    postorder = [9, 15, 7, 20, 3]
    res = Solution().buildTree(inorder, postorder)
    print(res)
