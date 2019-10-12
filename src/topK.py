# -*- encoding: utf-8 -*-

"""
大量数据中找topK个数

K的大小对应不同的策略，如果k很小，如果小于5，那么直接选择排序就可以。
"""
import random


def random_select(nums, left, right, k):
    """
    随机选择，受快速排序启发，如果能一次找到第k大的数，使得它左边都小于它，右边都大于它，那么答案就是右边那些。

    降序，这样的话直接定位k就可以了。
    :param nums:
    :param left:
    :param right:
    :param k:
    :return:
    """
    L, R = left, right
    idx = random.randint(L, R)
    pivot = nums[idx]
    nums[idx], nums[L] = nums[L], nums[idx]
    while L < R:
        while R > L and nums[R] <= pivot:
            R -= 1
        nums[L] = nums[R]
        while L < R and nums[L] >= pivot:
            L += 1
        nums[R] = nums[L]
    nums[L] = pivot
    if L == k:
        return nums[:L]
    elif L < k:
        return random_select(nums, L+1, right, k)
    else:
        return random_select(nums, left, L, k)


def heap(nums, k):
    """
    堆排序，堆的大小限制在K个
    :param nums:
    :param k:
    :return:
    """
    import heapq
    pq = []
    for num in nums:
        heapq.heappush(pq, num)
        if len(pq) > k:
            heapq.heappop(pq)
    return pq


if __name__ == '__main__':
    data = [i for i in range(1000)]
    random.shuffle(data)
    data2 = [i for i in data]
    res1 = random_select(data, 0, len(data)-1, 20)
    res2 = heap(data, 20)
    res1.sort()
    res2.sort()
    print(res1)
    print(res2)
    print(res1 == res2)



