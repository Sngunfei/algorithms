
"""
两个队列实现一个栈

每次弹出时，队列内元素都循环一遍，然后把最后的元素弹出来。
"""


class StackBasedQueue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, elem):
        self.queue1.append(elem)

    def size(self):
        return len(self.queue1)

    def pop(self):
        while self.queue1:
            cur = self.queue1.pop(0)
            if not self.queue1:
                self.queue1 = self.queue2
                self.queue2 = []
                return cur
            else:
                self.queue2.append(cur)


if __name__ == '__main__':
    stack = StackBasedQueue()
    for i in range(5):
        stack.push(i)
    print(stack.pop())
    print(stack.pop())
    for i in range(100, 110):
        stack.push(i)

    size = stack.size()
    for i in range(size):
        print(stack.pop())
    a = [1]
    b = [2]
    a.extend()


