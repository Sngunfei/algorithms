

"""
并查集
"""

class Node:

    def __init__(self, val):
        self.parent = self
        self.rank = 1
        self.val = val


def find(node):
    if node.parent == node:
        return node
    # 路径压缩
    node.parent = find(node.parent)
    return node.parent

def union(node1, node2):
    parent1, parent2 = find(node1), find(node2)
    if parent1 == parent2: # 已经在一个集合里
        return
    rank1, rank2 = parent1.rank, parent2.rank
    # 按秩合并
    if rank1 > rank2:
        parent2.parent = parent1
    elif rank2 > rank1:
        parent1.parent = parent2
    else:
        parent2.parent = parent1
        parent1.rank += 1


if __name__ == '__main__':
    arr = [[1, 2], [1, 3], [2, 4], [3, 5], [6, 7], [7, 8], [9, 10], [10, 8]]
    map = {}
    for pair in arr:
        a, b = pair
        node1, node2 = map.get(a, None), map.get(b, None)
        if not node1:
            node1 = Node(a)
            map[a] = node1
        if not node2:
            node2 = Node(b)
            map[b] = node2
        union(node1, node2)

    for key, val in map.items():
        print(key, val.parent.val)



