class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_total = total = sum(nums[:k])
        n = len(nums)
        for i in range(k, n):
            total = total + nums[i] - nums[i - k]
            max_total = max(total, max_total)
        return max_total / k


if __name__ == '__main__':
    print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))
