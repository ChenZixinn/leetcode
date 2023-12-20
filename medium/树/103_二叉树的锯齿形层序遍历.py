"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
"""
import collections
import queue
from typing import Optional, List

from common.data_structure import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        node_queue = collections.deque()
        node_queue.append(root)
        is_order_left = True
        while len(node_queue)>0:
            level_list = []
            for i in range(len(node_queue)):
                node = node_queue.popleft()
                if is_order_left:
                    level_list.append(node.val)
                else:
                    level_list.insert(0, node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            ans.append(level_list)
            is_order_left = not is_order_left
        return ans



if __name__ == '__main__':
    r5 = TreeNode(7)
    r4 = TreeNode(15)
    r3 = TreeNode(20,r4, r5)
    r2 = TreeNode(9)
    root = TreeNode(3, r2, r3)
    res = Solution().zigzagLevelOrder(root)
    print(res)