# -*- encoding:utf-8 -*-

"""
Chapter 21, 不相交集合的数据结构
"""

# 每个集合用链表实现
class _DS_node:
    def __init__(self, data=None):
        self.head = None # 所在集合的头结点
        self.next = None # 下一个节点
        self.data = data # 存放的数据

# 集合
class _DS_set:
    def __init__(self):
        self.head = None  # 集合的代表元素，第一个数据节点
        self.tail = None  # 链表尾部
        self.num = 0

def _make_set(x):
    _set = _DS_set()
    _node = _DS_node(data=x)
    _set.head = _node
    _set.tail = _node
    _set.num = 1
    return _set


def _find_set(node):
    """
    查找节点所在集合
    :param node: ds_node
    :return:
    """
    return node.head if node else None


def _union_set_list(set1, set2):
    """
    并操作的链表实现
    :param set1:
    :param set2:
    :return:
    """
    if not set1:
        return set2
    if not set2:
        return set1

    # 将短链表并入到长链表中
    if set1.num < set2.num:
        set1, set2 = set2, set1

    set1.tail.next = set2.head # 并入
    cur = set2.head
    while cur:
        cur.head = set1 # 修改各个节点的头指针
        if not cur.next:
            set1.tail = cur # 更新set1的尾指针
        cur = cur.next
    return set1

#################################################################################################################

"""
不相交集合森林，每个集合表现为一棵树

两种启发式优化策略：
1. 按秩合并， union by rank， 将高度较小的树并入到高度较高的树中
2. 路径压缩，查找路径中的每个节点直接指向根节点。
"""


class Node:
    def __init__(self, data):
        self.parent = self
        self.rank = 0
        self.data = data


def make_set(x):
    """
    创建集合
    :param x:
    :return:
    """
    node = Node(data=x)
    return node


def find_set(node):
    if node != node.parent:
        node.parent = find_set(node.parent) # 路径压缩
    return node


def _link(node1, node2):
    if not node1 or not node2:
        return node1 if node1 else node2

    if node1.rank >= node2.rank:
        node2.parent = node1
        if node1.rank == node2.rank:
            node1.rank += 1
        return node1
    else:
        node1.parent = node2
        return node2


def union_set(node1, node2):
    _link(find_set(node1), find_set(node2))



