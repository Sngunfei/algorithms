# -*- encoding :utf-8 -*-

"""
两个栈实现一个队列

一个栈负责进，一个栈负责出
"""


class QueueBasedStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, elem):
        self.stack1.append(elem)

    def pop(self):
        if self.stack2:
            return self.stack2.pop(-1)
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
            if self.stack2:
                return self.stack2.pop(-1)
        raise ValueError("数量不足")


if __name__ == '__main__':
    queue = QueueBasedStack()
    for i in range(10):
        queue.push(i)

    for i in range(5):
        print(queue.pop())

    for i in range(100, 120):
        queue.push(i)

    for i in range(25):
        print(queue.pop())

