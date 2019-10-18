# -*- encoding: utf-8 -*-

"""
最小生成树， Minimum Spanning Tree
"""

from .graph import Edge
from .disjoint_set import make_set, find_set, union_set
import heapq


def kruskal(edges):
    """
    最小生成树, kruskal算法，O（E * logV）
    集合A是一个森林，每次加入到A中的安全边，永远是连接两个不同分量的权重最小的边。

    贪心算法，每次都选择当前最小权重的边，先把所有边都排序，然后查看边两边的节点是否属于同一集合。
    :param: 图的边集合， [edges]
    :return:
    """
    edges_heap = []
    nodes = set()
    for edge in edges:
        heapq.heappush(edges_heap, (edge.weight, edge))
        nodes.add(edge.start)
        nodes.add(edge.end)

    nodes_set = dict()
    for node in nodes:
        nodes_set[node] = make_set(node)

    mst = set()
    while edges_heap:
        w, edge = heapq.heappop(edges_heap)
        start_node = nodes_set[edge.start]
        end_node = nodes_set[edges.end]

        if find_set(start_node) != find_set(end_node):
            mst.add(edge)
            union_set(start_node, end_node)

    return mst


def prim(edges):
    """
    最小生成树，prim算法
    集合A是一棵树，每次加入到A中的安全边，永远是连接A和A以外某个节点的最小权重边

    树中每次添加新节点时，都要去松弛其他节点。
    :return:
    """
    from collections import defaultdict
    import heapq

    adj = defaultdict(dict)  # 邻接表
    dist = {}
    prev = {}  # 前驱点

    root = None
    for edge in edges:
        u, v, w = edge.start, edge.end, edge.weight
        dist[u] = dist[v] = float("inf")
        prev[u] = prev[v] = None
        adj[u][v] = adj[v][u] = w

        if not root:
            root = u  #　随机选根

    dist[root] = 0
    vis = set()
    i = 0
    while i < len(adj):  # 直到弹出N个节点
        min_dist = float("inf")
        min_node = None
        for node, distance in dist.items():
            if node not in vis and distance < min_dist:
                min_node, min_dist = node, distance

        vis.add(min_node)
        for neighbor, weight in adj[min_node]:
            if neighbor not in vis and weight < dist[neighbor]:
                dist[neighbor] = weight
                prev[neighbor] = min_node

        i += 1

    mst = set()
    for node in vis:
        _pre = prev.get(node, None)
        if _pre:
            mst.add(Edge(_pre, node, adj[_pre][node]))
    return mst



if __name__ == '__main__':
    pass