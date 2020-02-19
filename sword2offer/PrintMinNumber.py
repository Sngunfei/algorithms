
"""
给定一个数组，里面存放一些正整数，求他们拼接后的最小值

如[3, 32, 321]，其能达到的最小值是321323

判断两个数字的情况，比如m，n，我们只需要找出mn和nm哪个小就可以了，多个数字同理，排序即可。
"""

from functools import cmp_to_key


def cmp(a, b):
    ab = a + b
    ba = b + a
    if ab == ba:
        return 0
    if ab > ba:
        return 1
    return -1


def printMinNumber(arr):
    arr = list(map(str, arr))
    arr.sort(key=cmp_to_key(cmp))
    ans = ""
    for num in arr:
        ans += num
    return ans


if __name__ == '__main__':
    arr = [3, 32, 321, 3210, 1, 2, 3]
    print(printMinNumber(arr))
