# -*- encoding:utf-8 -*-

"""
常用的图算法
"""

class Edge:
    def __init__(self, start, end, weight=1.0):
        self.start = start
        self.end = end
        self.weight = weight


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
    单源最短路径，bellman-ford算法
    :return:
    """
    pass


def floyd():
    """
    多源最短路径，floyd算法
    :return:
    """
    pass

