import time


def timer(f):
    """ Декоратор для замера времениработы функции"""
    def tmp(*args, **kwargs):
        begin = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print("Время выполнения функции: {}".format(end - begin))
        return res
    return tmp


@timer
def heapsort(iterable):
    """ Пирамидальная сортировка с использованием минимальной кучи из модуля heapq"""
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]

@timer
def bubble_sorting(alist: list) -> list:
    """
    Сортировка пузырьком

    :type alist: object
    :param collection (list): Список для сортировки
    :return:
            collection (list): Отсортированный список
    """
    N = len(alist)
    for i in range(N - 1):
        swapped = True
        for j in range(N - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                swapped = False
        if swapped:
            break
    return alist