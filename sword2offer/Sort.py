

"""
排序方法
"""
import random

def qsort(nums, left, right):
    if left >= right:
        return
    pos = random.randint(left, right)
    val = nums[pos]
    nums[pos], nums[left] = nums[left], nums[pos]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= val:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= val:
            i += 1
        nums[j] = nums[i]
    nums[i] = val
    qsort(nums, left, i-1)
    qsort(nums, i+1, right)

if __name__ == '__main__':
    arr = [random.randint(1, 1000) for _ in range(20)]
    qsort(arr, 0, len(arr)-1)
    print(arr)


