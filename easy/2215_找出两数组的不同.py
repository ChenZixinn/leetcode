from typing import List


class Solution:
    """
        给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，请你返回一个长度为 2 的列表 answer ，其中：

        answer[0] 是 nums1 中所有 不 存在于 nums2 中的 不同 整数组成的列表。
        answer[1] 是 nums2 中所有 不 存在于 nums1 中的 不同 整数组成的列表。
        注意：列表中的整数可以按 任意 顺序返回。

        来源：力扣（LeetCode）
        链接：https://leetcode.cn/problems/find-the-difference-of-two-arrays
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # 存放结果的二维数组
        answer = []
        set1 = set(nums1)
        set2 = set(nums2)
        answer.append([i for i in set1 if i not in set2])
        answer.append([i for i in set2 if i not in set1])
        return answer


if __name__ == '__main__':
    answer = Solution().findDifference([1, 2, 3, 3], [1, 1, 2, 2])
    print(answer)
