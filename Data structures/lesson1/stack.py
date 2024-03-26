class Stack:

    def __init__(self):
        self._data = []

    def push(self, value):
        """ добавление нового элемента в стек """
        self._data.append(value)

    def pop(self):
        """ удаление и возврат элемента в порядке «последним пришел, первым вышел» (Last In First Out – LIFO) """
        return self._data.pop()

    def peek(self):
        """ возврат очередного элемента в порядке «последним пришел, первым вышел» (LIFO) """
        return self._data[-1]

    def is_empty(self):
        """ возврат True, если в стеке нет элементов, иначе возврат False """
        return len(self._data) == 0


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
v = stack.pop()
print(v)
print(stack.peek())

while not stack.is_empty():
    print(stack.pop())
