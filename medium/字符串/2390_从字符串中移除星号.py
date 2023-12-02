class Solution:
    def removeStars(self, s: str) -> str:
        """
        给你一个包含若干星号 * 的字符串 s 。
        在一步操作中，你可以：

        选中 s 中的一个星号。
        移除星号 左侧 最近的那个 非星号 字符，并移除该星号自身。
        返回移除 所有 星号之后的字符串。

        来源：力扣（LeetCode）
        链接：https://leetcode.cn/problems/removing-stars-from-a-string
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        :param s: 带"*"的字符串
        :return: 处理后的字符串
        """
        l = []
        for i in s:
            if i == '*' and l:
                l.pop()
            else:
                l.append(i)
        return "".join(l)


if __name__ == '__main__':
    result = Solution().removeStars("12*3")
    print(result)