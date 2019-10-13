# -*- encoding: utf-8 -*-

"""
常用的哈希函数。

最完美的哈希函数应该能够将所有关键字均匀分布，即每个槽中都有 N / M个元素， N/M称为负载因子。

为了克服关键字背后的概率分布所带来的的影响，最好能引入随机因素，比如全域散列技术。

散列表的设计要从几个方面出发：
    - 关键字的个数，如果只有寥寥几个元素，直接数组定位即可。
    - 关键字是静态的，不涉及插入删除，只负责查找，则使用完全散列。
    - 尽量避免冲突，如果出现了冲突要选择合适的方法去解决。比如链接法和开放寻址法。
"""

class Hash:

    def __init__(self):
        self.arr = []
        self.size = 0


    @staticmethod
    def divide_hash(k, factor):
        """
        除法哈希，h(k) = k mod m
        :param k:
        :param factor:
        :return:
        """
        if factor == 0:
            raise ValueError("The factor of divide_hash_function can't be zero.")
        return k % factor


    @staticmethod
    def multiply_hash(k, factor, m):
        """
        h(k) = m(k*factor mod 1)
        :param k:
        :param factor: 常数因子， 0 < factor < 1
        :param m:
        :return:
        """
        # factor 可以为0，但此时会导致最坏性能。
        return int(m * (k * factor % 1))


    @staticmethod
    def universal_hash(hs, random_state, k):
        """
        全域哈希, 在一组哈希函数随机选取其中一个。
        :param hs: 哈希函数组, [callable]
        :param random_state: 随机种子
        :param k: 关键字
        :return:
        """
        import random
        random.seed(random_state)
        hash_f = hs[random.randint(0, len(hs)-1)]
        return hash_f(k)

    @staticmethod
    def _linear_probing(h, k, i, m):
        """
        线性探查
        :param h: callable, 辅助散列函数
        :param k: 关键字
        :param i:
        :param m:
        :return:
        """
        return (h(k) + i) % m

    @staticmethod
    def _quadratic_probing(h, k, i, m, c1, c2):
        """
        二次探查, 可以构造出 N 次探查，只要指定好参数即可。
        """
        return (h(k) + c1 * i + c2 * (i**2)) % m

    @staticmethod
    def double_hash(h1, h2, k, i, m):
        """
        双重哈希， 也可以构造出 N 重哈希。
        :param h1:
        :param h2:
        :param k:
        :param i:
        :param m:
        :return:
        """
        return (h1(k) + i * h2(k)) % m

    @staticmethod
    def open_address_hash(k):
        """
        开放寻址法, addr = h(k, i), k是关键字，i是探查次数，直到探查到空槽。
        :return:
        """
        pass

    @staticmethod
    def link_hash():
        """
        链接哈希，每个位置上的元素为链表。
        :return:
        """
        pass

    # todo
    @staticmethod
    def intelligent_hash(self):
        """
        智能哈希，从关键字构成的分布中学到一个分类器，惩罚项就是不同分类簇大小之间的差异。

        与其绞尽脑汁的设计哈希函数，不如收集关键字数据集去训练出一个哈希函数。
        :return:
        """
        raise NotImplementedError("Intelligent hash function.")
