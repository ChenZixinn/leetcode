"""
https://leetcode.cn/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

"""
from typing import Optional

from common.data_structure import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 非递归
        # if list1 == None:
        #     return list2
        # elif list2 == None:
        #     return list1
        # head = list1 if list1.val <= list2.val else list2
        # list1, list2 = (list1.next, list2) if list1.val <= list2.val else (list1, list2.next)
        # pre_list = head
        # while list1 != None and list2 != None:
        #     if list1.val <= list2.val:
        #         pre_list.next = list1
        #         list1 = list1.next
        #     else:
        #         pre_list.next = list2
        #         list2 = list2.next
        #     pre_list = pre_list.next
        # if list1 == None:
        #     pre_list.next = list2
        # elif list2 == None:
        #     pre_list.next = list1
        # return head

        # 递归
        if not list2: return list1
        if not list1: return list2
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


if __name__ == '__main__':
    l3 = ListNode(4)
    l2 = ListNode(3, l3)
    l1 = ListNode(1, l2)
    r3 = ListNode(4)
    r2 = ListNode(2, r3)
    r1 = ListNode(1, r2)
    res = Solution().mergeTwoLists(l1, r1)
    while res:
        print(res.val)
        res = res.next
