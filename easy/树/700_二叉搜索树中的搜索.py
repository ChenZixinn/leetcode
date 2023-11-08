from typing import Optional

from common.data_structure import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 递归方法
        if not root:
            return None
        if val == root.val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)

        # 迭代
        # while root is not None:
        #     if root.val == val:
        #         return root
        #     root = root.left if root.val > val else root.right
        # return None


if __name__ == '__main__':
    # root = [4,2,7,1,3], val = 2
    root = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val=7))

    result = Solution().searchBST(root, 3)
    print(result.val)