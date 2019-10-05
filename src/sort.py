
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
    pass


def quick_sort():
    pass


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
    bubble_sort()


