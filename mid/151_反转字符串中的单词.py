class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        while "  " in s:
            s = s.replace("  ", " ")
        ori_list = s.split()

        for i in range(len(ori_list)//2):
            left = ori_list[i]
            ori_list[i] = ori_list[len(ori_list)-i-1]
            ori_list[len(ori_list)-i-1] = left
        # return " ".join(ori_list)

        # 官方解答
        return " ".join(reversed(s.split()))


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("aaa   bbb ccc ddd"))