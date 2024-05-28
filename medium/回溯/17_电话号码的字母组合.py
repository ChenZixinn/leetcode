import itertools
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # 1、递归
        # def backtrace(index: int):
        #     if len(digits) == index:
        #         return combinations.append(''.join(combination))
        #     digit = digits[index]
        #     for letter in phoneMap[digit]:
        #         combination.append(letter)
        #         backtrace(index+1)
        #         combination.pop()
        #
        # combinations = list()
        # combination = list()
        # backtrace(0)

        # 2、迭代
        groups = (phoneMap[digit] for digit in digits)
        return [''.join(combination) for combination in itertools.product(*groups)]


if __name__ == '__main__':
    res = Solution().letterCombinations('242')
    print(res)
