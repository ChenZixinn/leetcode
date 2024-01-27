"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""
from typing import Optional

from common.data_structure import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # 双指针
        # dummy = ListNode(0, head)
        # first = head
        # second = dummy
        # # 这一步是为了和second保持距离，当first走到底时，second即指向了目标节点
        # for i in range(n):
        #     first = first.next
        # while first:
        #     first = first.next
        #     second = second.next
        # second.next = second.next.next
        # return dummy.next

        # 栈
        stack = list()
        dummy = ListNode(0, head)
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop()
        cur = stack.pop()
        cur.next = cur.next.next
        return dummy.next



if __name__ == '__main__':
    pass