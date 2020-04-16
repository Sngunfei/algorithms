
"""
不用四则运算，实现加法
"""


def add(a, b):
    while b:
        ans = a ^ b
        c = (a & b) << 1
        a, b = ans, c
    return a

if __name__ == '__main__':
    print(add(101, 202))