from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i = max(candies) - extraCandies
        return [candie >= i for candie in candies]


if __name__ == '__main__':
    result = Solution().kidsWithCandies([1, 6, 4, 2], 2)
    print(result)
