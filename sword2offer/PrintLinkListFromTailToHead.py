# -*- encoding: utf-8 -*-

"""
从尾到头打印队列

1. 修改原数据：翻转链表，O（n）
2. O（2n），可以先把结果存到数组里，然后把数组翻转一下。压栈，然后逐个弹出

栈可以改成递归形式，在当前位置上，调用递归函数打印后面的节点，然后再打印当前节点。
"""

def printLinkListFromTailToHead(head):
    if not head:
        return
    cur = head
    stack = []
    cnt = 0
    while cur:
        stack.append(cur.value)
        cur = cur.next
        cnt += 1

    while cnt > 0:
        print(stack[cnt - 1])
        cnt -= 1
