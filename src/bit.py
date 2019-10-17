


def find_1(nums):
    """
    找数组中只出现一次的数，其他数都出现两次，异或运算，a^b^b = a
    :param nums:
    :return:
    """
    ans = nums[0]
    for i in range(1, len(nums)):
        ans ^= nums[i]
    return ans


def find_2(nums):
    """
    数组中两个数各出现一次，其他数都出现两次，根据异或运算可以拿到a^b，
    然后根据某一位是否为1可以将所有数分成两组，a和b各在一组，并且组内其他的数都出现两次。
    :param nums:
    :return:
    """
    res = find_1(nums)
    power = 1
    while True:
        if res & power:
            break
        else:
            power <<= 1
    ans1, ans2 = res, res
    for num in nums:
        if num & power:
            ans1 ^= num  # a ^ b ^ a
        else:
            ans2 ^= num  # a ^ b ^ b
    return ans1, ans2



def find_3(nums):
    """
    找到数组中三个只出现一次的数，先找到一个位1，因为只有1/1/1或者1/0/0能够异或出一个1，所以按照这个
    位置来划分，可以得到两种结果，一种是1个1和两个0，这时候等价为find_1和find_@，如果是3个1，则需要再
    找到下一个位1的位置，继续判断。

    :param nums:
    :return:
    """
    res = find_1(nums)
    power = 1
    while True:
        if res & power:
            arr1, arr2 = [], []
            res1, res2 = 0, 0
            for num in nums:
                if num & power:
                    arr1.append(num)
                    res1 ^= num
                else:
                    arr2.append(num)
                    res2 ^= num
            if res1 and res2:
                if len(arr1) % 2 == 1:
                    ans1 = find_1(arr1)
                    ans2, ans3 = find_2(arr2)
                else:
                    ans1, ans2 = find_2(arr1)
                    ans3 = find_1(arr2)
                break
            else:  # 三个数的该位都是1，那么还需要往前找一个新的位置。
                power <<= 1
        else:
            power <<= 1

    return ans1, ans2, ans3


def find_N():
    """
    从一个数组中找到N个只出现一次的数，可行吗？
    :return:
    """
    raise NotImplementedError("find N")


def find_1_from_n(nums, n):
    """
    假如有一个数组，里面有一个数只出现了一次，而其他数都出现了n次。
    假设是int类型，那么32位，每一位上的1的个数都应该被n整除，如果不能，那就说明这个数字在该位上为1。
    :param nums:
    :param n:
    :return:
    """
    bits = [0] * 32
    power = 0
    while power < 32:
        curNum = 2 ** power
        for num in nums:
            bits[power] += curNum & num
        power += 1
    ans = 0
    for i in range(32):
        ans += 2**i if bits[i] % n else 0
    return ans



if __name__ == '__main__':
    import random
    data = [i for i in range(100)]
    data = data + data + data + data + data
    random.shuffle(data)
    data.insert(100, 1000)
    print(find_1_from_n(data, 5))

