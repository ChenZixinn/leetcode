"""
这题相当于有个棋盘，从左下角开始蛇形向上每个格子有个从1开始递增的序号，你从序号1的格子开始，你每步可以从当前格子开始往后走1~6格，
你只能按照序号的升序走，不能往回走（如第5格走到第4格），走到最后一格就结束了。每个格子内有传送门或啥都没有，-1代表啥都没有，大于0的数字代表传送门，
传送门意味着你可以传送到当前数字的格子去（如当前是35，你就可以传送到序号为35的格子去），如果你传送过去后的格子内依然是大于0的数字，你不能连续传送，
现在要求最少需要几步可以走到终点。
"""
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def id2rc(idx: int) -> (int, int):
            row = (idx - 1) // n
            col = (idx - 1) % n
            if row % 2 == 1:
                col = n - col - 1
            return n - 1 - row, col

        queue = list()
        queue.append((1, 0))
        vis = set()
        vis.add(1)
        while queue:
            idx, step = queue.pop(0)
            # 走6步
            for i in range(1, 6 + 1):
                idx_nxt = idx + i
                x_nxt, y_nxt = id2rc(idx_nxt)
                if idx_nxt > n * n:  # 超出边界
                    break
                if board[x_nxt][y_nxt] > 0:  # 存在蛇或梯子
                    idx_nxt = board[x_nxt][y_nxt]
                if idx_nxt == n * n:  # 到达重点
                    return step + 1
                if idx_nxt not in vis:  # 没访问过
                    vis.add(idx_nxt)
                    queue.append((idx_nxt, step + 1))  # 扩展新状态
        return -1


if __name__ == '__main__':
    # [[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]]
    board = [[-1, 1, 2, -1],
             [2, 13, 15, -1],
             [-1, 10, -1, -1],
             [-1, 6, 2, 8]]
    res = Solution().snakesAndLadders(board)
    print(res)
    #
    # n = len(board)
    #
    # def id2rc(idx: int) -> (int, int):
    #     row = (idx - 1) // n
    #     col = (idx - 1) % n
    #     if row % 2 == 1:
    #         col = n - col - 1
    #     return n - 1 - row, col
    #
    #
    # print(id2rc(6))
