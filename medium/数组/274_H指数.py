from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 排序
        n = len(citations)
        tot = 0
        counter = [0] * (n + 1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1

        for i in range(n, -1, -1):
            tot += counter[i]
            if tot >= i:
                return i
        return 0


        # 二分
        # citations.sort()
        # n = len(citations)
        # left = 0
        # right = n
        # while left < right:
        #     mid = (left + right + 1) >> 1
        #     tot = 0
        #     for c in citations:
        #         if c >= mid:
        #             tot += 1
        #     if tot >= mid:
        #         left = mid
        #     else:
        #         right = mid-1
        #
        # return left



if __name__ == '__main__':
    print(Solution().hIndex([1]))
    print(Solution().hIndex([3,0,6,1,5]))