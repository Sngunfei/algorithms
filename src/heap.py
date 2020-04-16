# -*- encoding:utf-8 -*-


def LEFT(i):
    return i << 1


def RIGHT(i):
    return (i << 1) + 1


def PARENT(i):
    return i >> 1


class Heap:

    def __init__(self, array):
        self.A = [-1] + array
        self.heap_size = len(array)
        self.build_heap()

    def max_heapify(self, i):
        """
        维护堆的性质
        :param i:
        :return:
        """
        L = LEFT(i)
        R = RIGHT(i)
        largest = L if L <= self.heap_size and self.A[L] > self.A[i] else i
        largest = R if R <= self.heap_size and self.A[R] > self.A[largest] else largest
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.max_heapify(largest)

    def build_heap(self):
        """
        建堆
        :return:
        """
        for i in range(len(self.A)//2, 0, -1):
            self.max_heapify(i)

    def print_heap(self):
        queue = [1]
        i = 0
        while queue:
            size = len(queue)
            nodes = []
            for _ in range(size):
                index = queue.pop(0)
                nodes.append(str(self.A[index]))
                if LEFT(index) <= self.heap_size:
                    queue.append(LEFT(index))
                if RIGHT(index) <= self.heap_size:
                    queue.append(RIGHT(index))
            print(i, ":  ", ",".join(nodes))
            i += 1

    def heap_sort(self):
        """
        堆排序，每次弹出根节点，然后维护堆的性质。
        弹出根节点就是将根节点与末端节点互换，然后再重新建一次堆
        :return:
        """
        for i in range(len(self.A)-1, 0, -1):
            self.A[1], self.A[i] = self.A[i], self.A[1]
            self.heap_size -= 1
            self.max_heapify(1)

    def pq_max(self):
        return self.A[1]

    def pq_extract_max(self):
        ans = self.A[1]
        self.A[1] = self.A[self.heap_size]
        self.heap_size -= 1
        self.max_heapify(1)
        return ans


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 20, 31, 23, 4, 5, 6, 12, 0, 12, 32, 4, 5]

    heap = Heap(arr)
    heap.print_heap()
    #heap.heap_sort()
    heap.pq_max()
    print(heap.heap_size)
    print(heap.pq_extract_max())
    print(heap.heap_size)
    print(heap.pq_extract_max())
    print(heap.heap_size)
    print(heap.pq_extract_max())
    print(heap.heap_size)
    import heapq
    heapq.heappush()















