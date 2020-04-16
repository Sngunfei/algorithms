
"""
k-皇后
"""
import copy

def queens(mat, prevs, cur, k, res):
    if k == 0:
        res.append(copy.deepcopy(mat))
        return
    n = len(mat)
    x = cur
    for y in range(n):
        flag = True
        for prev_x, prev_y in prevs:
            if prev_y == y or abs(x-prev_x) == abs(y-prev_y):
                flag = False
                break
        if flag:
            mat[x][y] = 1
            queens(mat, prevs+[[x, y]], cur+1, k-1, res)
            mat[x][y] = 0

if __name__ == '__main__':

    a = "0123"
    a = a.lstrip("0")
    print(a)


