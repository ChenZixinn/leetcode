"""
https://leetcode.cn/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10-5 以内的答案可以被接受。
"""
from typing import List, Optional

from common.data_structure import TreeNode


class Solution:
    def __init__(self):
        self.ans = []
        self.count = []

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def dfs(root: Optional[TreeNode], level: int):
            if not root:
                return
            if len(self.ans)-1 >= level:
                self.count[level] += 1
                self.ans[level] += root.val
            else:
                self.ans.append(root.val)
                self.count.append(1)
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return [ans/count for ans, count in zip(self.ans, self.count)]

if __name__ == '__main__':
    # [3,1,5,0,2,4,6]
    r4 = TreeNode(0)
    r5 = TreeNode(2)
    r6 = TreeNode(4)
    r7 = TreeNode(6)
    r2 = TreeNode(1, r4, r5)
    r3 = TreeNode(5, r6, r7)
    r1 = TreeNode(3, r2, r3)
    res = Solution().averageOfLevels(r1)
    print(res)