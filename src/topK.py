# -*- encoding: utf-8 -*-

"""
大量数据中找topK个数

K的大小对应不同的策略，如果k很小，如果小于5，那么直接选择排序就可以。
"""

# todo
def random_select(nums):
    """
    随机选择，受快速排序启发，如果能一次找到第k大的数，使得它左边都小于它，右边都大于它，那么答案就是右边那些。
    :param nums:
    :return:
    """
    pass


def heap(nums):
    """
    堆排序，堆的大小限制在K个
    :param nums:
    :return:
    """
    pass




