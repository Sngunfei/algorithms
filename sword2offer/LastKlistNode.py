
"""
找到链表中倒数第k个节点

相关问题：
1. 找到链表中间位置的节点
2. 判断是否是环形链表，并计算环形的长度
"""

from ListNode import ListNode


def findLast_k_NodeFromList(head: ListNode, k):
    if not head or k == 0:
        return None
    """
    1->2->3->4->5， k=2
    因为要找到倒数第k个，这个与尾节点之间差k-1步
    """
    fast = head
    for i in range(k-1):
        if not fast.next:
            return None
        fast = fast.next

    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next

    return slow


def findMidPosition(head: ListNode):
    if not head:
        return None
    fast = head.next
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def isCircle(head: ListNode):
    """
    判断是否具有环形结构，如果是，返回环形的起点，否则返回False

    快慢指针肯定是在环形结构上的某一处相遇，注意此时快指针是“绕了一圈”才追上慢指针的，

    令开头未参与环形的长度为L，即环形的起始位置为L，两者在环形上的位置距离L为k
    则快指针走了2（L+k）步，慢指针走了L+k步，快指针走了一次L，并且k的区域走了两次，
    那么剩余区域就为L，圆的周长为L+k，所以此时再开一个指针，和慢指针同时走，两者相遇
    刚好走过L步，即为环形的起始位置
    :param head:
    :return:
    """
    if not head:
        return None
    fast = head.next
    slow = head
    while fast and fast.next:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next

    slow = slow.next  # 这一步很重要，因为这相当于环形的起点
    cnt = 0
    ans = head
    while True:
        if ans == slow:
            return ans
        ans = ans.next
        slow = slow.next
        cnt += 1


if __name__ == '__main__':
    head = ListNode(0)
    cur = head
    nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    tmp = None
    for i in range(10):
        node = ListNode(nums[i])
        cur.next = node
        cur = cur.next
        if i == 5:
            tmp = cur

    #print(findLast_k_NodeFromList(head, 3).val)
    print(findMidPosition(head.next).val)
    #print(isCircle(head.next).val)

