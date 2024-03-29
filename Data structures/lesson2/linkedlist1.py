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
        self._length = 0

    def add_first(self, item):
        self._head = Node(item, self._head)
        self._length += 1

    def add_last(self, item):
        if self._head is None:
            self._head = Node(item, self._head)
        else:
            cursor = self._head
            while cursor.link is not None:
                cursor = cursor.link
            cursor.link = Node(item, None)

        self._length += 1

    def remove_first(self):
        if self._head is None:
            raise
        item = self._head.data
        self._head = self._head.link
        self._length -= 1
        return item

    def remove_last(self):
        if self._head is None:
            raise
        if self._head.link is None:
            item = self._head.data
            self._head = self._head.link
            self._length -= 1
            return item
        else:
            cursor = self._head
            while cursor.link.link is not None:
                cursor = cursor.link
            item = cursor.link.data
            cursor.link = None
            self._length -= 1
            return item

    def __len__(self):
        return self._length

    def items(self):
        if self._head is None:
            return
        cursor = self._head
        while cursor.link is not None:
            print(cursor.data)
            cursor = cursor.link
        print(cursor.data)


head = Node(1,
            Node(2,
                 Node(3,
                      Node(4, None))))

linked_list = LinkedList()
linked_list.add_last(1)
linked_list.add_last(2)
linked_list.add_last(3)
linked_list.add_last(4)

linked_list = LinkedList()
linked_list.add_last(1)
linked_list.add_first(0)
linked_list.add_last(2)
linked_list.items()
linked_list.remove_first()
linked_list.remove_last()
linked_list.remove_first()
linked_list.items()
