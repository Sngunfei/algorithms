
"""
给定一个数组，统计其内部的逆序对个数

归并排序

两个排好序的数组，如何统计逆序数？只需要每次复制的时候，把另一个数组中的剩余个数统计一下，
那么等复制完，这个数字就是答案了。那问题来了，如何得到两个排好序的数组呢？
"""

def mergeSort(nums, left, right):
    """
    归并排序
    :param nums:
    :param left:
    :param right:
    :return:
    """
    if left >= right:
        return 0
    mid = left + ((right - left) >> 1)

    cnt_left = mergeSort(nums, left, mid)
    cnt_right = mergeSort(nums, mid+1, right)

    left_nums = nums[left:mid+1]
    right_nums = nums[mid+1:right+1]
    i = len(left_nums) - 1
    j = len(right_nums) - 1
    index = right
    cnt = 0
    while i >= 0 and j >= 0:
        if left_nums[i] > right_nums[j]:
            nums[index] = left_nums[i]
            cnt += j + 1
            i -= 1
        else:
            nums[index] = right_nums[j]
            j -= 1
        index -= 1

    while j >= 0:
        nums[index] = right_nums[j]
        j -= 1
        index -= 1
    while i >= 0:
        nums[index] = left_nums[i]
        i -= 1
        index -= 1

    return cnt_left + cnt_right + cnt


def merge_sort(nums, left, right):
    """
    原地归并排序
    :param nums:
    :param left:
    :param right:
    :return:
    """
    if left == right:
        return

    mid = left + (right - left) >> 1
    merge_sort(nums, left, mid)
    merge_sort(nums, mid+1, right)

    i = mid
    j = right
    index = right
    ni, nj = nums[i], nums[j]
    while i >= left and j >= mid + 1:
        if ni > nj:
            nums[index] = ni
            i -= 1
            ni = nums[i]
        else:
            nums[index] = nj
            j -= 1
            nj = nums[j]
        index -= 1

    while i >= left:
        nums[index] = nums[i]
        i -= 1
        index -= 1
    while j >= mid + 1:
        nums[index] = nums[j]
        j -= 1
        index -= 1


def cnt_inverse_pairs(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
    return cnt


if __name__ == '__main__':
    arr = [7, 4, 6, 5, 1, 2, 3, 4, 7, 8, 9, 2, 10]
    res = [0] * len(arr)
    print(cnt_inverse_pairs(arr))
    print(mergeSort(arr, 0, len(arr) - 1))
    print(arr)
