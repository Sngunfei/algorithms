
"""
二分查找
"""

def binarySearch(arr, target):

    L, R = 0, len(arr) - 1
    while L <= R:
        mid = (L + R) >> 1
        if arr[mid] > target:
            R = mid - 1
        elif arr[mid] < target:
            L = mid + 1
        else:
            return mid
    if arr[L] == target:
        return L
    return -1

if __name__ == '__main__':
    import random
    arr = [random.randint(1, 100) for _ in range(20)]
    target = arr[5]
    arr.sort()
    print(target)
    print(arr)
    print(binarySearch(arr, target))

