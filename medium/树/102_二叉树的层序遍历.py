"""

"""
from typing import Optional, List

from common.data_structure import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            num = len(queue)
            level_res = []
            for _ in range(num):
                root = queue.pop(0)
                level_res.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(level_res)
        return res


if __name__ == '__main__':
    r7 = TreeNode(7)
    r8 = TreeNode(8)
    r9 = TreeNode(9)
    r4 = TreeNode(4)
    r5 = TreeNode(5, r7)
    r6 = TreeNode(6, r8, r9)
    r2 = TreeNode(2, r4, r5)
    r3 = TreeNode(3, r6)
    root = TreeNode(3, r2, r3)
    res = Solution().levelOrder(root)
    print(res)