"""
有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，其中points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。

一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。

给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。


示例 1：

输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：气球可以用2支箭来爆破:
-在x = 6处射出箭，击破气球[2,8]和[1,6]。
-在x = 11处发射箭，击破气球[10,16]和[7,12]。
示例 2：

输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
解释：每个气球需要射出一支箭，总共需要4支箭。
示例 3：

输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：气球可以用2支箭来爆破:
- 在x = 2处发射箭，击破气球[1,2]和[2,3]。
- 在x = 4处射出箭，击破气球[3,4]和[4,5]。
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if not points:
            return 0
        """ 1.排序+贪心算法 """
        # 排序,从小到大
        points.sort(key=lambda p: p[1])
        # 选一支箭，一只箭最小的标准是要能射到第一个区域的最右侧距离（请看__main__中的注释）
        pos = points[0][1]
        ans = 1
        for i in points:
            if i[0] > pos:
                # 如果射不到，新建一只箭，同样是射到当前距离的极限距离
                pos = i[1]
                ans += 1
        return ans

        """ 2.找最小交集 """
        # points.sort()
        # res = []
        # for i in points:
        #     if not res or res[-1][1] < i[0]:
        #         res.append(i)
        #     else:
        #         res[-1][0] = i[0]
        #         res[-1][1] = min(res[-1][1], i[1])
        # return len(res)


if __name__ == '__main__':
    title = [[1,2],[2,3],[3,4],[4,5]]
    res = Solution().findMinArrowShots(title)
    """
       |
    [1,2]  |
      [2,3]|
       |[3,4]
       |  [5,6]
           |
    """
    print(res)
