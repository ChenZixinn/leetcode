from common.data_structure import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, path_max):
            if root == None:
                return 0
            res = 0
            if root.val >= path_max:
                path_max = root.val
                res += 1
            res += dfs(root.left, path_max) + dfs(root.right, path_max)
            return res
        return dfs(root, -10**9)



if __name__ == '__main__':
    r1 = TreeNode(3)
    r2 = TreeNode(1)
    r3 = TreeNode(5)
    r4 = TreeNode(1, left=r1)
    r5 = TreeNode(4, left=r2, right=r3)
    root = TreeNode(3, r4, r5)
    good_nodes_sum = Solution().goodNodes(root)
    print(good_nodes_sum)
