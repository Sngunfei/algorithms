# -*- encoding:utf-8 -*-

"""
一个矩阵，每行都是从左到右升序排列
每列是从上到下升序。

整个矩阵有偏序关系, 从这样一个矩阵中找到目标数组target

消除查找范围，每次消灭一列或者一行
"""
import numpy as np

def findInPartiallySortedMatrix(matrix: list, target):
    m, n = len(matrix), len(matrix[0])
    cur_x, cur_y = 0, n-1
    print(target)
    cnt = 0
    while cur_x < m and cur_y >= 0:
        cur_num = matrix[cur_x][cur_y]
        print(cnt, cur_x, cur_y, cur_num)
        if cur_num == target:
            return cur_x, cur_y
        elif cur_num > target:
            # 在左边，不可能在下边
            cur_y -= 1
        elif cur_num < target:
            cur_x += 1
        cnt += 1

    return -1, -1


if __name__ == '__main__':
    matrix = np.asarray([[1, 2, 8, 9],
                         [2, 4, 9, 12],
                         [4, 7, 10, 13],
                         [6, 8, 11, 15]])
    res = findInPartiallySortedMatrix(matrix, 7)
    print(res)
    print(matrix[res])

