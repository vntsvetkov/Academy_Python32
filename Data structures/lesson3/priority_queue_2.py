class Element:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"(Значение {self.item}; Приоритет {self.priority})"


class ListPriorityQueue:
    def __init__(self):
        self._queue: list[Element] = []

    def __str__(self):
        return ' '.join([str(i) for i in self._queue])

    def is_empty(self):
        return len(self._queue) == 0

    def insert1(self, item):
        self._queue.append(item)
        self._queue.sort()

    def delete1(self):
        return self._queue.pop().item

    def insert2(self, item):
        self._queue.append(item)

    def delete2(self):
        m = self._queue[0].priority
        i = 0
        for index in range(1, len(self._queue)):
            if self._queue[index].priority > m:
                m = self._queue[index].priority
                i = index

        self._queue[i], self._queue[-1] = self._queue[-1], self._queue[i]
        return self._queue.pop().item


pq = ListPriorityQueue()
pq.insert1(Element(1, 1))
pq.insert1(Element(2, 2))
pq.insert1(Element(3, 0))
print(pq.delete2())
