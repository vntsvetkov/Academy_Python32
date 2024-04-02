from heapq import heapify, heappush, heappop


class BinMinHeap:

    def __init__(self, data=None):
        if data is None:
            self._data = []
        else:
            self._data = [e for e in data]
            heapify(self._data)

    @property
    def data(self):
        return self._data

    def insert(self, item):
        heappush(self._data, item)

    def delete(self):
        return heappop(self._data)

    def peek(self):
        return self._data[0]


# heap = BinMinHeap([0, 4, 9, 7, 1, 2])
# print(heap.data)
# print(heap.delete())
# print(heap.delete())
# print(heap.delete())
# print(heap.delete())
