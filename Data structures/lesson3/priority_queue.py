
class ListPriorityQueue:
    def __init__(self):
        self._queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self._queue])

    def is_empty(self):
        return len(self._queue) == 0

    def insert1(self, item):
        self._queue.append(item)
        self._queue.sort()

    def delete1(self):
        return self._queue.pop()

    def insert2(self, item):
        self._queue.append(item)

    def delete2(self):
        m = self._queue[0]
        i = 0
        for index in range(1, len(self._queue)):
            if self._queue[index] > m:
                m = self._queue[index]
                i = index

        self._queue[i], self._queue[-1] = self._queue[-1], self._queue[i]
        return self._queue.pop()


pq = ListPriorityQueue()
pq.insert1(1)
pq.insert1(4)
pq.insert1(0)
pq.insert1(2)
pq.insert1(3)
print(pq)

print(pq.delete2())

