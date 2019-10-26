# -*- encoding: utf-8 -*-

"""
Dynamic Programming, 其中programming是指表格，而不是指程序。

分治用来解决子问题不重叠的情况，然后各自解决单个小问题，最后把结果拼在一起即可。
当子问题重叠的时候，分治就会重复计算很多次某些子问题，效率低下，需要用动态规划的方法。

设计一个动态规划的算法有四个步骤：
1. 刻画问题最优解的结构特征
2. 递归地定义最优解的值
3. 计算最优解的值，自底向上
4. 依据第三步的表格构造出最优解
"""

profit = [float("-inf") for _ in range(100)]
profit[0] = 0
def cut_rod(n, p):
    """
    钢条切割问题
    :param n: 钢条的长度，int， >= 0
    :param p: 价格表，长度为index的钢条的价格， list[float]
    :return: 最优切割方案，最大利润。
    """
    if profit[n] >= 0:
        return profit[n]

    ans = float("-inf")
    for i in range(1, n+1):
        ans = max(ans, p[i] + cut_rod(n-i, p))

    profit[n] = ans
    return ans


def cut_rod_bottom_up(n, p):
    """
    自底向上的解法
    :param n:
    :param p:
    :return:
    """
    s = [0] * (n + 1)
    for j in range(1, n+1):
        ans = float("-inf")
        for i in range(1, j+1):
            if ans < p[i] + profit[j-i]:
                ans = p[i] + profit[j-i]
                s[j] = i  # 长度为j的钢条，最优切割方案里的 第一段钢条 的长度
        profit[j] = ans

    rods = []
    length = n
    while length > 0:
        rods.append(s[length])
        length -= s[length]

    return rods, profit[n]


def cut_rod_test():
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(cut_rod_bottom_up(4, p))



def matrix_link(matrices):
    """
    矩阵链乘, 先设置初始长度为2，然后逐渐增加，然后在长度为length的[i, ..., j]里，找到合适的分割点k
    :param matrices: [[m, n], ...]
    :return:
    """
    size = len(matrices)
    cost = [[float("inf")] * size for _ in range(size)]
    for i in range(size):
        cost[i][i] = 0
    s = [[0] * size for _ in range(size)]
    for length in range(2, size+1):
        for i in range(size-length+1):
            j = i + length - 1
            for k in range(i, j):
                _cost = cost[i][k] + cost[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
                if _cost < cost[i][j]:
                    cost[i][j] = _cost
                    s[i][j] = k
    return cost, s


def matrix_link_test():
    matrices = [[10, 100], [100, 5], [5, 50], [50, 30]]
    cost, s = matrix_link(matrices)
    print(cost)
    size = len(matrices)

    def _func(matrix, i, j):
        if i > j:
            return ""
        if i == j:
            return "A{}".format(i)
        k = matrix[i][j]
        print(i, j, k)
        if k == i:
            return "(A{}{})".format(i, _func(matrix, i+1, j))
        return "{}{}".format(_func(matrix, i, k), _func(matrix, k+1, j))

    print(_func(s, 0, size-1))
    print(cost[0][size - 1])



if __name__ == '__main__':
    matrix_link_test()