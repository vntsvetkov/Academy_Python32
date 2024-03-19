from abc import ABC, abstractmethod

"""
Создайте базовый абстрактный класс ChessFigure. Опишите следующие
методы:

- Определить бьет ли она другую фигуру на поле
- Сделать ход на поле
- Определить возможность хода по правилам
- Определить текущие координаты

1. Создайте класс HorseFigure - наследника, класса ChessFigure
2. Сделайте ход на поле по правилам
3. Определить сможет ли ваша фигура побить другую
"""


class ChessFigure(ABC):

    @abstractmethod
    def is_beats(self, coord: tuple) -> bool:
        ...

    @abstractmethod
    def move(self, coord: tuple) -> None:
        ...

    @abstractmethod
    def check_move(self, coord: tuple) -> bool:
        ...

    @abstractmethod
    def get_coord(self) -> tuple:
        ...


class HorseFigure(ChessFigure):

    def __init__(self, column: str, row: str):
        self.column = column
        self.row = row

    def __validate_row(self):
        ...

    def __validate_column(self):
        ...

    def get_coord(self) -> tuple:
        return self.column, self.row

    def check_move(self, coord: tuple) -> bool:
        x1 = ord(self.column) % 8
        y1 = int(self.row)

        if ord(coord[0]) < 65 or ord(coord[0]) > 72:
            raise ValueError("Ошибка диапазона от A до H")
        if int(coord[1]) < 1 or int(coord[1]) > 8:
            raise ValueError("Ошибка диапазона от 1 до 8")

        x2 = ord(coord[0]) % 8
        y2 = int(coord[1])

        x = abs(x2 - x1)
        y = abs(y2 - y1)

        return (x == 2 and y == 1) or (x == 1 and y == 2)

    def move(self, coord: tuple) -> None:
        try:
            if self.check_move(coord):
                self.column, self.row = coord
            else:
                print(f"""Ход в {coord[0]}{coord[1]} невозможен""")
        except ValueError as e:
            print(f"""Ход в {coord[0]}{coord[1]} невозможен""")

    def is_beats(self, coord: tuple) -> bool:
        x1 = ord(self.column) % 8
        y1 = int(self.row)

        x2 = ord(coord[0]) % 8
        y2 = int(coord[1])

        x = abs(x2 - x1)
        y = abs(y2 - y1)

        return (x == 2 and y == 1) or (x == 1 and y == 2)


def f(figure: ChessFigure):
    horse = HorseFigure('E', '4')
    other_horse = HorseFigure('D', '5')
    print(horse.is_beats(other_horse.get_coord()))
    # horse.move(('D', '5'))
    # print(horse.get_coord())


class SystemUser(ABC):

    _in_system = False

    @abstractmethod
    def info(self):
        ...

    @abstractmethod
    def log_in(self):
        ...

    @abstractmethod
    def log_out(self):
        ...

    @abstractmethod
    def change_password(self, password: str):
        ...


class Employee(SystemUser):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def info(self):
        return (f"Логин: {self.login}\n"
                f"Пароль: {self.password}")

    def change_password(self, password: str):

        if self.password == password:
            raise ValueError("Новый пароль не может совпадать с текущим")

        self.password = password
        # Отправить запрос на изменение данных пользователя

    def log_in(self):
        # Надо выполнить проверку существования пользователя
        if not self._in_system:
            self._in_system = True
            print("Вход выполнен")
        else:
            print("Пользователь уже вошел в систему")

    def log_out(self):

        if self._in_system:
            self._in_system = False
            print("Выход выполнен")
        else:
            print("Пользователь уже вышел из системы")


employee = Employee('login', 'password')
print(employee.info())
employee.change_password('other_password')
print(employee.info())


def loging(emp: SystemUser):
    emp.log_in()


loging(employee)


class Shape(ABC):
    ...


class Circle(Shape):
    file_name = "Окружности.txt"
    ...


class Square(Shape):
    file_name = "Квадраты.txt"
    ...


shapes = [Circle(), Square()]


def func(shape: Shape):
    ...


for shape in shapes:
    func(shape)