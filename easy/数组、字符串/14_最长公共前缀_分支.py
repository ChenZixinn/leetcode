"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 分支算法
        def lcp(start, end):
            if start == end:
                return strs[start]
            mid = (start + end) // 2
            left_lcp, right_lcp = lcp(start,mid), lcp(mid+1, end)
            min_length = min(len(left_lcp), len(right_lcp))
            for i in range(min_length):
                if left_lcp[i] != right_lcp[i]:
                    return left_lcp[:i]
            return left_lcp[:min_length]

        return "" if not strs else lcp(0, len(strs) - 1)


if __name__ == '__main__':
    res = Solution().longestCommonPrefix(["flower", "flow", "flight"])
    print(res)