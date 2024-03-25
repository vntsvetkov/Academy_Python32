class Time:

    def __init__(self, h, m, s):
        self.__h = h  # валидация
        self.__m = m  # валидация
        self.__s = s  # валидация

    @classmethod
    def from_seconds(cls, seconds: int):
        s = seconds % 60
        m = seconds // 60 % 60
        h = seconds // 3600 % 24
        return cls(h, m, s)

    def __lt__(self, other) -> bool:
        if isinstance(other, Time):
            return int(self) < int(other)
        if isinstance(other, int):
            return self.__get_seconds() < other
        raise TypeError(f"'<' не поддерживается между типами Time and {other.__class__.__name__}")

    def __eq__(self, other) -> bool:
        if isinstance(other, Time):
            return int(self) == int(other)
        if isinstance(other, int):
            return self.__get_seconds() == other
        raise TypeError(f"'==' не поддерживается между типами Time and {other.__class__.__name__}")

    def __get_seconds(self) -> int:
        return self.__s + self.__m * 60 + self.__h * 3600

    def __int__(self):
        return self.__s + self.__m * 60 + self.__h * 3600

    def __str__(self):
        hh = str(self.__h // 10) + str(self.__h % 10)
        mm = str(self.__m // 10) + str(self.__m % 10)
        ss = str(self.__s // 10) + str(self.__s % 10)
        return f"{hh}:{mm}:{ss}"

    def __hash__(self):
        return hash((self.__h, self.__m, self.__s))

    def __add__(self, other):
        if isinstance(other, (Time, int)):
            new_time = int(self) + int(other)
            return Time.from_seconds(new_time)

        raise TypeError(f"'+' не поддерживается между типами Time and {other.__class__.__name__}")

    def __sub__(self, other):
        if isinstance(other, (Time, int)):
            new_time = int(self) - int(other)
            return Time.from_seconds(new_time)

        raise TypeError(f"'-' не поддерживается между типами Time and {other.__class__.__name__}")

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return self - other


t1 = Time(10, 0, 0)
t2 = Time(11, 0, 0)

t3 = t1 + t2
t4 = t1 - t2
t5 = t1 + 3600
t6 = t1 - 3600
t7 = 3600 + t1
t8 = 3600 - t1

# t1 += t2
# print(t1)
# t1 -= t2
# print(t1)
# t2 += 3600
# print(t2)
# t2 -= 3600
# print(t2)