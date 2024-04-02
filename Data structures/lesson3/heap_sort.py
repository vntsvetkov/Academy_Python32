from min_heap import BinMinHeap
import heapq


class Element:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"(Значение {self.item}; Приоритет {self.priority})"


def heapsort(data):
    x = []
    heap = BinMinHeap(data)
    while heap.data:
        x.append(heap.delete())
    return x


lst = [Element(1, 2), Element(2, 0)]
t = []
heapq.heapify(lst)
while lst:
    t.append(heapq.heappop(lst).item)

print(t)

# print(heapsort(lst))
