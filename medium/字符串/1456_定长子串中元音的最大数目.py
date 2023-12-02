# 给你字符串 s 和整数 k 。
#
# 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
#
# 英文中的 元音字母 为（a, e, i, o, u）。
#
# https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(ch):
            """
            判断是否为元音，返回1/0
            :param ch: 字符
            :return: 1是元音，0非元音
            """
            return int(ch in 'aeiou')

        n = len(s)
        # 先找前面k个的结果数
        vowel_count = sum(1 for i in range(k) if is_vowel(s[i]))
        ans = vowel_count
        # 从找过的地方开始，往前推，后面往前走；有三种情况
        # 右侧新进入窗口的字母为元音字母，左侧移出窗口的字母也是元音字母，这样一进一出抵消掉了
        # 右侧新进入窗口的字母为元音字母，左侧移出窗口的字母非元音字母，此时元音字母个数+1
        # 右侧新进入窗口的字母非元音字母，左侧移出窗口的字母为元音字母，此时元音字母个数-1
        for i in range(k, n):
            vowel_count += is_vowel(s[i]) - is_vowel(s[i - k])
            ans = max(vowel_count, ans)
        return ans


if __name__ == '__main__':
    print(Solution().maxVowels("abciiidef", 3))
