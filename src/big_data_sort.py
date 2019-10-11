# -*- encoding:utf-8 -*-

"""
大数据排序，一百亿个int排序

先哈希，存到各个文件里，然后对文件排序，然后用堆将元素挨个取出。

如果已经有文件了，就省略哈希这一步，直接对文件进行排序。

如果内存限制小于文件大小，那么还需要分块排序，比如把一个大文件拆分成小文件。

"""


def hash_nums(nums, n_files):
    """

    :param nums: 全部数字
    :param n_files: 哈希成多少份
    :return:
    """
    files = []
    for i in range(n_files):
        files.append(open("../data/nums_{}.txt".format(i), encoding="utf-8", mode="w+"))

    for number in nums:
        files[number % n_files].write("{} \n".format(number))

    for file in files:
        file.close()

    print("Hash Done.")


def reduce(n_files):
    import heapq
    pq = []
    for i in range(n_files):
        fin = open("../data/nums_sort_{}.txt".format(i), encoding="utf-8", mode="r")
        _num = int(fin.readline().strip())
        heapq.heappush(pq, (_num, fin))

    res = open("../data/result.txt", encoding="utf-8", mode="w+")

    while pq:
        num, fin = heapq.heappop(pq)
        res.write("{} \n".format(num))
        _num = fin.readline().strip()
        if _num:
            heapq.heappush(pq, (int(_num), fin))
        else:
            fin.close()

    print("Reduce Done.")


def single_file_sort(file_idx):

    from src.sort import quick_sort

    fin = open("../data/nums_{}.txt".format(file_idx), encoding="utf-8", mode="r")
    nums = []

    while True:
        line = fin.readline().strip()
        if not line:
            break
        nums.append(int(line))
    fin.close()

    quick_sort(nums)

    fout = open("../data/nums_sort_{}.txt".format(file_idx), encoding="utf-8", mode="w+")
    for num in nums:
        fout.write("{} \n".format(num))
    fout.close()

    print("File {} sort done.".format(file_idx))


def files_sort(n_files):
    for idx in range(n_files):
        single_file_sort(idx)

    print("All files sort done.")


def generate_nums(n=1000000, limit=100000000):
    """
    产生n个数，默认为100万。
    :param n:
    :param limit: 数的范围
    :return:
    """
    import random
    nums = [random.randint(0, limit) for _ in range(n)]
    return nums


if __name__ == '__main__':
    nums = generate_nums()
    hash_nums(nums, 10)
    files_sort(10)
    reduce(10)











