"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""
from typing import Optional

from common.data_structure import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sortFunc(head, tail):
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while tail != fast:
                slow = slow.next
                fast = fast.next
                if tail != fast:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1, head2):
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        return sortFunc(head, None)


if __name__ == '__main__':
    l4 = ListNode(3)
    l3 = ListNode(1, l4)
    l2 = ListNode(2, l3)
    head = ListNode(4, l2)
    res = Solution().sortList(head)
    print(res)
