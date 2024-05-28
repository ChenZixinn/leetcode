"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""
from typing import List


class Solution:
    def max_heapify(self, a: list, i: int, heap_size: int):
        l = i * 2 + 1
        r = i * 2 + 2
        largest = i
        if l < heap_size and a[l] > a[largest]:
            largest = l
        if r < heap_size and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.max_heapify(a, largest, heap_size)

    def build_max_heapify(self, a: list, heap_size: int):
        for i in range(heap_size // 2, -1, -1):
            self.max_heapify(a, i, heap_size)

    def quick_sort(self, nums, l, r, k):
        if l == r:
            return nums[l]
        i = l - 1
        j = r + 1
        partition = nums[l]
        while i < j:
            i += 1
            while (nums[i] < partition):
                i += 1
            j -= 1
            while (nums[j] > partition):
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        if k <= j:
            return self.quick_sort(nums, l, j, k)
        else:
            return self.quick_sort(nums, j + 1, r, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        找到数组中第 k 大的元素。

        :param nums: List[int] - 输入数组。
        :param k: int - 要找到的第 k 大的位置。
        :return: int - 第 k 大的元素。
        """
        # 1、快速排序实现
        n = len(nums)
        return self.quick_sort(nums, l=0, r=n - 1, k=n - k)

        # 2、堆排序实现()
        # heap_size = len(nums)
        # self.build_max_heapify(nums, heap_size)
        # for i in range(heap_size-1, heap_size-k, -1):
        #     nums[0], nums[i] = nums[i], nums[0]
        #     heap_size -= 1
        #     self.max_heapify(nums, 0, heap_size)
        # return nums[0]


if __name__ == '__main__':
    res1 = Solution().findKthLargest([3, 2, 1, 5, 6, 4], k=2)
    print(res1)
    # res2 = Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4)
    # print(res2)
