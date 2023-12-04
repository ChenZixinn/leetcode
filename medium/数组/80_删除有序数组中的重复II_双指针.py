"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。



说明：

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}


示例 1：

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 计数
        # left, right = 0, 0
        # pre, count = nums[0], 0
        # while right < len(nums):
        #     if nums[right] == pre:
        #         count += 1
        #         if count > 2:
        #             right += 1
        #             continue
        #     else:
        #         pre = nums[right]
        #         count = 1
        #     nums[left] = nums[right]
        #     left += 1
        #     right += 1
        # return left

        # 快慢指针
        n = len(nums)
        slow, fast = 2,2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

if __name__ == '__main__':
    l = [1, 1, 1, 1, 2, 2, 3]
    res = Solution().removeDuplicates(l)
    print(res)
    print(l)
