

"""
找到最小的k个数字，topK，快速选择
"""


def qselect(nums, left, right, k):
    if left >= right:
        return

    pos = (left + right) >> 1
    val = nums[pos]
    nums[pos], nums[left] = nums[left], nums[pos]
    L, R = left, right

    while L < R:
        while L < R and nums[R] >= val:
            R -= 1
        nums[L] = nums[R]
        while L < R and nums[L] <= val:
            L += 1
        nums[R] = nums[L]
    nums[L] = val
    if L < k:
        qselect(nums, L+1, right, k)
    elif L > k:
        qselect(nums, left, L-1, k)
    else:
        return

if __name__ == '__main__':
    import random
    arr = [random.randint(1, 1000) for _ in range(50)]
    qselect(arr, 0, len(arr) - 1, 10)
    print(arr[:10])
    print(sorted(arr)[:10])