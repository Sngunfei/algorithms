
"""
翻转链表

"""
from ListNode import ListNode

def reverseList(head: ListNode):
    if not head:
        return None
    cur = head
    prev = None
    while cur:
        _next = cur.next
        if not _next:
            head = cur
        cur.next = prev
        prev = cur
        cur = _next

    return head


if __name__ == '__main__':
    head = ListNode(0)
    cur = head
    for i in range(10):
        node = ListNode(i)
        cur.next = node
        cur = cur.next

    head = reverseList(head.next)
    while head:
        print(head.val)
        head = head.next

