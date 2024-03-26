class Queue:

    def __init__(self):
        self._data = []

    # enqueue(item) – добавление нового элемента в очередь.
    def enqueue(self, item):
        self._data.append(item)

    # dequeue() – удаление и возврат элемента в порядке «первым пришел, первым вышел» (First In First Out – FIFO).
    def dequeue(self):
        return self._data.pop(0)

    # peek() – возврат(без удаления) очередного элемента в очереди в порядке FIFO.
    def peek(self):
        return self._data[0]

    # is_empty() – возврат True, если в очереди нет элементов, иначе возврат False.
    def is_empty(self):
        return len(self._data) == 0


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.peek())
v = queue.dequeue()
print(v)

while not queue.is_empty():
    print(queue.dequeue())
