
"""
两个链表交叉，找到其交叉起点。

1. 用两个栈，分别压到尾节点，然后一起弹出，只到弹出不同的节点，上一个即是答案。
2. 分别扫描长度，然后让较长的链表先走k步
"""
from Nodes import ListNode

def findFirstCommonNode_stack(list1, list2):
    stack1, stack2 = [], []

    head = list1
    while head:
        stack1.append(head)
        head = head.next
    head = list2
    while head:
        stack2.append(head)
        head = head.next
    prev = None
    while stack1 and stack2:
        top1, top2 = stack1.pop(-1), stack2.pop(-1)
        if top1 == top2:
            prev = top1
            continue
        else:
            break
    return prev


def findFirstCommonNode_scan(list1, list2):
    len1, len2 = 0, 0
    cur = list1
    while cur:
        len1 += 1
        cur = cur.next
    cur = list2
    while cur:
        len2 += 1
        cur = cur.next
        
    k = abs(len1 - len2)
    if len1 < len2:
        list1, list2 = list2, list1

    for _ in range(k):
        list1 = list1.next

    while list1 and list2:
        if list1 == list2:
            return list1
        else:
            list1, list2 = list1.next, list2.next





if __name__ == '__main__':
    list1 = ListNode(0)
    cur = list1
    for i in range(1, 5):
        cur.next = ListNode(i)
        cur = cur.next

    list2 = ListNode(10)
    cur = list2
    for i in range(10, 15):
        cur.next = ListNode(i)
        cur = cur.next
    cur.next = list1

    list3 = ListNode(20)
    cur = list3
    for i in range(20, 25):
        cur.next = ListNode(i)
        cur = cur.next
    cur.next = list1

    node = findFirstCommonNode_scan(list2, list3)
    if node:
        print(node.val)