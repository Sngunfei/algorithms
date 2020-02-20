
"""
一个排序好的数组里，查询k的出现次数

- 二分查找到k的位置，然后往前搜，往后搜，把长度加起来
- 利用二分查找找到k的边界位置
"""

def getBoundaryK(arr, k, mode):
    L, R = 0, len(arr)-1
    while L <= R:
        mid = (L + R) >> 1
        if arr[mid] > k:
            R = mid - 1
        elif arr[mid] < k:
            L = mid + 1
        else:
            if mode == "left":
                if mid > 0 and arr[mid-1] == k:
                    R = mid - 1
                else:
                    return mid
            elif mode == "right":
                if mid < len(arr) - 1 and arr[mid+1] == k:
                    L = mid + 1
                else:
                    return mid
    if arr[L] == k:
        return L
    return - 1


if __name__ == '__main__':
    import random
    arr = [random.randint(1, 1000) for _ in range(20)]
    target = arr[5]
    arr =  arr + [target] * 10
    arr.sort()
    print(arr)
    L, R = getBoundaryK(arr, target, "left"), getBoundaryK(arr, target, "right")
    print(L, R - L + 1)