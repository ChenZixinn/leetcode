"""

给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

"""
from typing import Optional

from common.data_structure import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy_head = ListNode(0, head)
        cur = dummy_head
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next


if __name__ == '__main__':
    # 1,2,3,3,4,4,5
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))

    # 1,1,1,2,3
    head2 = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
    head3 = ListNode(1, ListNode(1))
    res = Solution().deleteDuplicates(head1)
    res2 = Solution().deleteDuplicates(head2)
    res3 = Solution().deleteDuplicates(head3)
