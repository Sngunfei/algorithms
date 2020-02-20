
"""
丑数，2,3,5

每次只找下一个丑数在哪，就是比当前数组末尾的丑数大，但是又最小。

因为每个丑数都是2,3,5的公倍数，我们可以把当前丑数数组中的每一个分别乘以2,3,5，

比如现在数组中有N个丑数，那么我们分别相乘后会得到3N个新丑数，然后找到它中间最小的就可以了。

但是这样效率会越来越低，我们真的需要用2,3,5去乘以数组中所有数字吗？

拿2举例，某个丑数为a，当前最大丑数为M，那么2*a无非有2种结果：

- 2a <= M: 此时2a已经在序列中了
- 2a > M，此时2a是下一个丑数的候选者

我们要找到这样一个位置p，使得：
在p之前的丑数，乘以2后都在序列内，在p之后的丑数，乘以2已经比下一个丑数要大，同理3,5也有这样位置。
"""


def uglyNumber(k: int):
    nums = [1]
    pos2, pos3, pos5 = 0, 0, 0

    for _ in range(k):
        candidate2, candidate3, candidate5 = nums[pos2] * 2, nums[pos3] * 3, nums[pos5] * 5
        next_ugly = min(candidate2, candidate3, candidate5)
        nums.append(next_ugly)
        while nums[pos2] * 2 <= nums[-1]:
            pos2 += 1
        while nums[pos3] * 3 <= nums[-1]:
            pos3 += 1
        while nums[pos5] * 5 <= nums[-1]:
            pos5 += 1
    return nums


if __name__ == '__main__':
    print(uglyNumber(10))