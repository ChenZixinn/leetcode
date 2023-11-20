"""
https://leetcode.cn/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def plus(index, num):
            if index == -1:
                digits.insert(0, num)
            else:
                new_num = digits[index] + 1
                if new_num >= 10:
                    digits[index] = new_num % 10
                    plus(index-1, new_num-9)
                else:
                    digits[index] = new_num
        plus(len(digits)-1, 1)
        return digits


if __name__ == '__main__':
    res = Solution().plusOne([9, 9, 9])
    print(res)