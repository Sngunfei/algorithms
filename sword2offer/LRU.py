

"""
实现LRU算法
"""

class DoubleListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LRU:

    def __init__(self, size):
        self._map = {}
        self._head = None
        self._tail = None
        self.maxSize = size
        self.size = 0

    def replaceHead(self, node):
        # 把某个节点放在双向链表的头部
        prev = node.prev
        next = node.next
        prev.next = next
        if next:  # node != tail
            next.prev = prev
        else:
            self._tail = prev

        node.next = self._head
        node.prev = None
        self._head.prev = node
        self._head = node


    def save(self, val):
        if val in self._map:
            # 放在链表头部
            node = self._map[val]
            self.replaceHead(node)
            self._map[val] = self._head
        else:
            node = DoubleListNode(val)
            self._map[val] = node
            if not self._head:
                self._head = node
                self._tail = node
                self.size = 1
            else:
                node.next = self._head
                self._head.prev = node
                self._head = node
                self._map[val] = node
                self.size += 1

            if self.size > self.maxSize:
                tail_value = self._tail.val
                self._map.pop(tail_value)

                prev = self._tail.prev
                prev.next = None
                self._tail = prev

                self.size -= 1

    def get(self, val):
        if val in self._map:
            node = self._map[val]
            self.replaceHead(node)
            return node
        else:
            raise ValueError("There does not exist value: {}\n".format(val))


    def printCurState(self):
        cur = self._head
        state = []
        while cur:
            state.append(cur.val)
            cur = cur.next
        print(state)


if __name__ == '__main__':
    lru = LRU(size=5)
    lru.save(1)
    lru.save(3)
    lru.save(5)
    lru.save(7)
    lru.save(9)
    lru.printCurState()
    lru.get(1)
    lru.get(3)
    lru.printCurState()
    lru.get(9)
    lru.printCurState()
    lru.save(10)
    lru.get(3)
    lru.printCurState()

