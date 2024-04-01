class Element:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"(Значение {self.item}; Приоритет {self.priority})"


class PriorityQueue:
    def __init__(self):
        self._queue: list[Element] = []

    def __str__(self):
        return ' '.join([str(i) for i in self._queue])

    def is_empty(self):
        ...

    def insert(self, item, priority):
        ...

    def delete(self):
        ...
