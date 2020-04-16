
"""
链表节点的定义
"""


class ListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SkipListNode:

    def __init__(self, key, val, level):
        self.key = key
        self.val = val
        self.level = level
        self.forwards = None # 各层的后序节点，数组容量为maxLevel





