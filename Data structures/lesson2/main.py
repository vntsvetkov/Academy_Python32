from collections import deque

"""
Дека (deque) - двусторонняя очередь

"""

d = deque()
d.append(1)
d.appendleft(0)

print(d)

d.pop()
d.popleft()

print(d)
