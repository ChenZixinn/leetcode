"""
给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，其中 intervals[i] = [starti, endi] 表示第 i 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end] 表示另一个区间的开始和结束。

在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。

返回插入之后的 intervals。

注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。



示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False  # 标记位，确保插入一次
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 有交集，计算并集
                left = min(left, li)
                right = max(ri, right)

        if not placed:
            ans.append([left, right])
        return ans


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    res = Solution().insert(intervals, newInterval)
    print(res)
