"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
"""
from typing import Optional

from common.data_structure import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head
        # 根据长度和翻转次数可以求出在第几个节点开始整体转移，不需要遍历多次翻转
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        # 计算偏移量
        if (add := n - k % n) == n:
            return head

        # 根据计算出来的偏移量翻转链表
        cur.next = head
        while add:
            add -= 1
            cur = cur.next
        ret = cur.next
        cur.next = None

        return ret


if __name__ == '__main__':
    k = 2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # head = ListNode(0, ListNode(1, ListNode(2)))
    new_head = Solution().rotateRight(head, k)
    print(new_head)
