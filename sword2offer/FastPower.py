
"""
快速幂
"""

def pow(num, x):
    res = 1
    cur = num
    while x:
        if x & 1:
            res *= cur
        cur *= cur
        x >>= 1
    return res


def matrix_pow(matrix, power):
    n = len(matrix)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1

    if power == 0:
        return ans

    def matrix_product(mat1, mat2):
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res

    cur = matrix
    while power:
        if power & 1:
            ans = matrix_product(ans, cur)
        cur = matrix_product(cur, cur)
        power >>= 1
    return ans


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix_pow(a, 7))
    import numpy as np
    cur = a
    for i in range(6):
        cur = np.matmul(cur, a)
    print(cur)