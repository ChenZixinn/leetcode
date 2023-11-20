"""
https://leetcode.cn/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划，台阶数0时[0]=1, [1]=1, [2]=2, [3]=3, [4]=[4-1]+[4-2]
        a, b = 1, 1
        for _ in range(n-1):
            a, b = b, a+b

        return b


if __name__ == '__main__':
    res = Solution().climbStairs(4)
    print(res)