# -*- encoding: utf-8 -*-
import random


def merge_sort():
    arr1 = [i for i in range(0, 100, 2)]
    arr2 = [i for i in range(1, 100, 2)]

    arr = []
    idx, idx1, idx2 = 0, 0, 0
    length = len(arr1) + len(arr2)

    while idx < length:

        if idx1 == len(arr1):
            while idx2 < len(arr2):
                arr.append(arr2[idx2])
                idx += 1
                idx2 += 1
            continue

        if idx2 == len(arr2):
            while idx1 < len(arr1):
                arr.append(arr1[idx1])
                idx += 1
                idx1 += 1
            continue

        if arr1[idx1] <= arr2[idx2]:
            arr.append(arr1[idx1])
            idx1 += 1
        elif arr1[idx1] > arr2[idx2]:
            arr.append(arr2[idx2])
            idx2 += 1
        idx += 1

    print(arr)


def selection_sort():
    pass


def heap_sort():
    # /src/heap
    pass


def quick_sort():
    arr = [i for i in range(100)]
    random.shuffle(arr)

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

    print(arr)
    _quicksort(arr, 0, len(arr) - 1)
    print(arr)


def bubble_sort():
    arr = [i for i in range(100)]
    random.shuffle(arr)

    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


def bucket_sort():
    pass


def insertion_sort():
    pass


if __name__ == '__main__':
    quick_sort()


