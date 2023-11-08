from common.data_structure import ListNode

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归实现(内存消耗较大)
        # 1. 递归函数的作用：反转链表head，并返回反转后的头结点
        # 2. 递归终止条件：head为空或者head.next为空
        # 3. 递归函数内部：head.next.next = head; head.next = None
        # 4. 返回值：反转后的头结点
        # if not head or not head.next:
        #     return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head

        # 迭代实现(内存消耗小)
        # 1. 定义一个新的头结点new_head，指向None
        # 2. 遍历链表，将每个节点的next指向new_head，然后将new_head指向当前节点
        # 3. 遍历结束后，返回new_head
        new_head = None
        while head:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node



