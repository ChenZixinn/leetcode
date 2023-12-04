# Definition for singly-linked list.
from typing import Optional

from common.data_structure import ListNode


class Solution:
    """
    给你一个链表的头节点 head 。

        长度为 n 链表的中间节点是从头数起第 ⌊n / 2⌋ 个节点（下标从 0 开始），其中 ⌊x⌋ 表示小于或等于 x 的最大整数。

        对于 n = 1、2、3、4 和 5 的情况，中间节点的下标分别是 0、1、1、2 和 2 。

        来源：力扣（LeetCode）
        链接：https://leetcode.cn/problems/delete-the-middle-node-of-a-linked-list
        著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

    """

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        删除 链表的 中间节点 ，并返回修改后的链表的头节点 head 。快慢指针
        复杂度分析
        时间复杂度：O(n)。
        空间复杂度：O(1)。
        :param head: 链表头节点
        :return: 删除中间节点后的头节点
        """
        # 只有一个节点直接返回
        if not head.next:
            return None
        slow, fast, pre = head, head, None
        while fast and fast.next :
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = pre.next.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    last = head
    for i in [3, 4, 7, 1, 2, 6]:
        now = ListNode(i)
        last.next = now
        last = last.next

    result = Solution().deleteMiddle(head)

    print_list = head
    while print_list is not None:
        print(print_list.val, end=' ')
        print_list = print_list.next
