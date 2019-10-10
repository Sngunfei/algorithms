

class ListNode:
    def __init__(self, val=-1):
        self.val = val
        self.next = None


def reverse_list(head):
    """
    翻转链表
    :param head:
    :return:
    """
    cur = head
    head = ListNode()
    head.next = cur

    while cur and cur.next:
        tmp = cur.next
        cur.next = tmp.next
        tmp.next = head.next
        head.next = tmp

    return head.next


def print_list(head):
    tmp = head
    res = ""
    while tmp:
        res += "{} ".format(tmp.val)
        tmp = tmp.next
    print(res)


if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    for i in range(2, 50):
        cur.next = ListNode(i)
        cur = cur.next
    print_list(head)
    head = reverse_list(head)
    print_list(head)
