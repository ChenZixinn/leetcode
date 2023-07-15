class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_ = 0
        g = 0
        for i in gain:
            g = g + i
            max_ = max(g, max_)
        return max_


if __name__ == '__main__':
    test = Solution().largestAltitude([-5,1,5,0,-7])
    print(test)