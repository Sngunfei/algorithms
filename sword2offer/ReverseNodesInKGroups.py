
"""
以k为一组，翻转链表
"""

from Nodes import ListNode
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = head
        prev = dummy

        i = 1
        while cur.next:
            cur = cur.next
            i += 1
            if i % k == 0:
                # 断链
                after = cur.next
                cur.next = None

                # 一直翻转到链表末尾
                start = prev.next
                while start.next:
                    tmp = start.next
                    start.next = tmp.next
                    tmp.next = prev.next
                    prev.next = tmp

                # 将断链重新接上
                prev = start
                start.next = after
                cur = start
        return dummy.next

