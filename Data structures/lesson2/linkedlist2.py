class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


"""
LinkedList или связный список – это структура данных. 
Связный список обеспечивает возможность создать двустороннюю очередь из каких-либо элементов. 
Каждый элемент такого списка считается узлом (Node). 
В каждом узле есть его значение, а также две ссылки – на предыдущий и на последующий узлы. 
То есть список «связывается» узлами, которые помогают двигаться вверх или вниз по списку. 
Из-за таких особенностей строения из связного списка можно организовать стек, очередь или двустороннюю очередь.
"""


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def add_first(self, item):
        self._head = Node(item, self._head)
        if self._tail is None:
            self._tail = self._head

    def add_last(self, item):
        if self._head is None:
            self._head = Node(item, self._head)
            if self._tail is None:
                self._tail = self._head
        else:
            self._tail.link = Node(item)
            self._tail = self._tail.link

    def remove_first(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        return item

    def remove_last(self):

        if self._head.link is None:
            item = self._head.data
            self._head = self._head.link
            if self._head is None:
                self._tail = None
            return item
        else:
            cursor = self._head
            while cursor.link is not self._tail:
                cursor = cursor.link
            item = self._tail.data
            self._tail = cursor
            self._tail.link = None
            return item

    def __len__(self):
        return self._length
