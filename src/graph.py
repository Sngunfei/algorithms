# -*- encoding:utf-8 -*-

"""
常用的图算法
"""

class Edge:
    def __init__(self, start, end, weight=1.0, directed=False):
        self.start = start
        self.end = end
        self.weight = weight
        self.directed = directed


class Graph:
    def __init__(self, edges):

        self.edges = edges
        self.n_edge = len(edges)
        self._create_node_map()



    def _create_node_map(self):
        self.node2idx = {}
        self.idx2node = {}
        idx = 0
        for edge in self.edges:
            u, v = edge.start, edge.end
            if u not in self.node2idx:
                self.node2idx[u] = idx
                self.idx2node[idx] = u
                idx += 1
            if v not in self.node2idx:
                self.node2idx[v] = idx
                self.idx2node[idx] = v
                idx += 1

    def get_link_matrix(self):
        """
        获取图的邻接矩阵形式
        :return:
        """
        if





def bfs():
    """
    广搜，队列，复杂度O(V + E)
    :return:
    """
    pass


def dfs():
    """
    深搜，栈，O(V + E)
    :return:
    """
    pass


def topological_sort():
    """
    有向无环图（DAG），拓扑排序，O(V + E)
    :return:
    """
    pass


def dijkstra():
    """
    单源最短路径，dijkstra
    :return:
    """
    pass



def bellman_ford():
    """
    单源最短路径，bellman-ford算法, 《算法导论》24.1, P379
    :return:
    """
    pass


def floyd():
    """
    多源最短路径，floyd算法
    :return:
    """
    pass


def maximum_flow():
    """
    最大流
    :return:
    """
    pass

