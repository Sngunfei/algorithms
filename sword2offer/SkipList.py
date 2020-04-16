

"""
跳表

每一层都是有序的，但是上面几层的数据是稀疏的，类似于B+树，上面层充当着索引的作用

扩建层是根据概率的
"""

from Nodes import SkipListNode
import random


class SkipList:

    maxLevel = 16

    def __init__(self):
        self.curLevel = 0
        # 头部起点，建层
        self.dummy = SkipListNode(-1, -1, self.maxLevel)
        self.dummy.forwards = [None for _ in range(self.maxLevel + 1)]


    def insert(self, key, val):
        cur = self.dummy
        # prev记录该节点在各层的前驱节点
        prev = [None for _ in range(self.maxLevel + 1)]
        for i in range(self.curLevel, -1, -1):
            while cur.forwards[i] and cur.forwards[i].key < key:
                cur = cur.forwards[i]
            prev[i] = cur
        cur = cur.forwards[0] # 最底层
        if cur and cur.key != key:
            level = 0
            # 使得各层的节点数量呈指数分布，1/2，1/4，1/8，...
            while random.randint(0, 1) == 0 and level < self.maxLevel:
                level += 1

            # 如果比当前层数大，则用头部节点补齐update数组
            if level > self.curLevel:
                for i in range(self.curLevel + 1, level + 1):
                    prev[i] = self.dummy
                self.curLevel = level

            newNode = SkipListNode(key, val, level)
            newNode.forwards = [None for _ in range(level + 1)]
            # 逐层加入新节点
            for i in range(level + 1):
                newNode.forwards[i] = prev[i].forwards[i]
                prev[i].forwards[i] = newNode
        else:
            cur.val = val


    def delete(self, key):
        """
        删除节点，和插入类似，先找各层前驱，然后删掉
        :param key:
        :return:
        """
        cur = self.dummy
        prev = [None for _ in range(self.maxLevel + 1)]
        for i in range(self.curLevel, -1, -1):
            while cur.forwards[i] and cur.forwards[i].key < key:
                cur = cur.forwards[i]
            prev[i] = cur
        cur = cur.forwards[0]
        if not cur or cur.key != key:
            return # 节点不存在
        for i in range(cur.level + 1):
            prev[i].forwards[i] = cur.forwards[i]

        # 节点删除可能会影响当前层数
        while self.curLevel > 0 and self.dummy.forwards[self.curLevel] is None:
            self.curLevel -= 1


    def find(self, key):
        cur = self.dummy
        for i in range(self.curLevel, -1, -1):
            while cur.forwards[i] and cur.forwards[i].key < key:
                cur = cur.forwards[i]
        cur = cur.forwards[0]
        if cur and cur.key == key:
            return cur.val
        return None







