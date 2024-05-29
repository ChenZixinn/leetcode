"""
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

示例 1：

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
示例 2：

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def get_num(index: int)->int:
            """
            返回数组下标对应的数据，由于二分查找的下标可能会等于n或者等于-1，需要进行处理
            :param index:
            :return:
            """
            if index == -1 or index == n:
                return float('-inf')
            return nums[index]
        l, r, ans = 0, n-1, 0
        while l <= r:
            mid = (l + r) // 2
            # 如果当前的值大于两边，则直接返回结果
            if get_num(mid - 1) < get_num(mid) > get_num(mid + 1):
                ans = mid
                break
            elif get_num(mid) > get_num(mid - 1):
                # 大于左边，往右找
                l = mid+1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    nums = [1, 2]
    res = Solution().findPeakElement(nums)
    print(res)