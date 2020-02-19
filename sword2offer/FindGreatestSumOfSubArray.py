
"""
连续子数组的最大和
"""


def findGreatestSumOfSubArray(arr):

    maxSum = float("-inf")
    cur = 0
    for i in range(len(arr)):
        if cur < 0:
            cur = arr[i]
        else:
            cur += arr[i]
        maxSum = max(maxSum, cur)

    return maxSum


def findGreatestSumOfSubArray_DP(arr):
    """
    动态规划解法
    转移函数：
    D[i] = num[i] + D[i-1] or num[i]
    :param arr:
    :return:
    """
    D = [0] * len(arr)
    max_sum = float("-inf")
    for idx, num in enumerate(arr):
        if idx == 0:
            D[idx] = arr[idx]
            continue
        D[idx] = max(D[idx-1] + arr[idx], arr[idx])
        max_sum = max(max_sum, D[idx])
    return max_sum


if __name__ == '__main__':
    arr = [1, -2, 3, 10, -4, 7, 2, -5]
    print(findGreatestSumOfSubArray_DP(arr))
