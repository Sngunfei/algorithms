# -*- encoding: utf-8 -*-
import random
import multiprocessing


def _merge(A, p, q, r):
    arr = []
    idx, idx1, idx2 = 0, p, q+1

    while idx1 <= q and idx2 <= r:
        if A[idx1] < A[idx2]:
            arr.append(A[idx1])
            idx1 += 1
        else:
            arr.append(A[idx2])
            idx2 += 1

    while idx1 <= q:
        arr.append(A[idx1])
        idx1 += 1
    while idx2 <= r:
        arr.append(A[idx2])
        idx2 += 1

    for i, element in enumerate(arr):
        A[p+i] = element


def merge_sort(A, p, r):
    if p < r:
        q = p + ((r-p) >> 1)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        _merge(A, p, q, r)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > element:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = element


def heap_sort():
    # /src/heap
    pass


def quick_sort(arr):
    def _quicksort(A, left, right):
        if left >= right:
            return
        pivot_idx = random.randint(left, right)
        pivot = A[pivot_idx]
        A[pivot_idx], A[left] = A[left], A[pivot_idx]
        L, R = left, right

        while L < R:
            while R > L and A[R] >= pivot:
                R -= 1
            A[L] = A[R]
            while L < R and A[L] <= pivot:
                L += 1
            A[R] = A[L]
        A[L] = pivot

        _quicksort(A, left, L-1)
        _quicksort(A, L+1, right)

    _quicksort(arr, 0, len(arr) - 1)


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bucket_sort():
    pass


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx, min_val = i, arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_idx = j
        if min_idx != i:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
            print(arr)


def indexSort(arr):
    """
    基数排序，对数字的每一位进行一次桶排序。
    :param arr:
    :return:
    """
    maxIndex = 0
    for num in arr:
        index = 0
        while num:
            num //= 10
            index += 1
        maxIndex = max(maxIndex, index)
    cnt = 0
    while cnt < maxIndex:
        bucket = [[] for _ in range(10)]
        for num in arr:
            cur = num
            i = 0
            while i < cnt:
                cur //= 10
                i += 1
            bucket[cur % 10].append(num)
        idx = 0
        for _bucket in bucket:
            for num in _bucket:
                arr[idx] = num
                idx += 1
        cnt += 1


if __name__ == '__main__':
    arr = [random.randint(1, 1000) for _ in range(20)]
    print(arr)
    indexSort(arr)
    print(arr)


