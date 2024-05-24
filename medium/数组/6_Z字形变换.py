"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);


示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
"""

"""
n=行数
间隔的行=n-2

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 列数小于2可以直接返回
        if numRows < 2:
            return s
        # 分为n列的数组
        res = ["" for _ in range(numRows)]
        # i为下标，flag为进退的值(1/-1)
        i, flag = 0, -1
        for c in s:
            # 将符号添加到对应的数组位置中
            res[i] += c
            # 为0后往前进，到底后往后退
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)


if __name__ == '__main__':
    inp = "PAYPALISHIRING"
    res = Solution().convert(inp, 3)
    print(res)
