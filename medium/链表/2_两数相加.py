"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""
from typing import Optional

from common.data_structure import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            total = n1 + n2 + carry
            if not head:
                tail = head = ListNode(val=total % 10)
            else:
                tail.next = ListNode(val=total % 10)
                tail = tail.next
            carry = total // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            tail.next = ListNode(val=carry)
        return head


if __name__ == '__main__':
    l1 = ListNode(9, next=ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    res = Solution().addTwoNumbers(l1, l2)
    print(res)