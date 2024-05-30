"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。
示例 1：

输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
示例 2：

输入：head = [2,1], x = 2
输出：[1,2]
"""
from typing import Optional

from common.data_structure import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 构建两条子链，链表不会增加内存消耗
        small = ListNode(0)
        small_head = small
        large = ListNode(0)
        large_head = large
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next
        # 小链表后面拼接上大链表
        large.next = None
        small.next = large_head.next
        # 返回小链表的节点
        return small_head.next




if __name__ == '__main__':
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    res = Solution().partition(head, 3)
    print(res)