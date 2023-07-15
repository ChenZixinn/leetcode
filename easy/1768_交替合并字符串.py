class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        m, n = len(word1), len(word2)
        i = 0
        word_list = []
        while i < m or i < n:
            if i < m:
                word_list.append(word1[i])
            if i < n:
                word_list.append(word2[i])
            i += 1
        return "".join(word_list)


if __name__ == '__main__':
    print(Solution().mergeAlternately("ace", "bdf"))