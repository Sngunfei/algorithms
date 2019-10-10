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


if __name__ == '__main__':
    arr = [i for i in range(10)]
    random.shuffle(arr)
    print(arr)
    selection_sort(arr)
    print(arr)


