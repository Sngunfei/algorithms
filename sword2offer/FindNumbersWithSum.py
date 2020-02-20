
"""

给定一个有序数组，和一个target，找出两个数组a和b，使得a+b=target，如果有多对，任意输出一对
"""

def findNumbersWithSum(arr, target):
    if target < arr[0] or target > arr[-1]:
        return
    L, R = 0, len(arr) - 1
    while L < R:
        if arr[L] + arr[R] > target:
            R -= 1
        elif arr[L] + arr[R] < target:
            L += 1
        else:
            return arr[L], arr[R]


if __name__ == '__main__':
    import random
    arr = [random.randint(1, 100) for _ in range(30)]
    target = arr[12] + arr[15]
    print(target)
    arr.sort()
    print(arr)
    print(findNumbersWithSum(arr, target))