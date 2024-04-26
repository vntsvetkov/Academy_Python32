class CalculateAreaFigures:
    from math import pi

    @staticmethod
    def area_square(side: float):
        if not isinstance(side, (float, int)):
            raise TypeError("Сторона квдрата должна быть числом")
        if side < 0:
            raise ValueError("Сторона квадрата не может отрицательной")
        return side ** 2

    @staticmethod
    def area_rectangle(side_a: float, side_b: float):
        return side_a * side_b

    @staticmethod
    def area_circle(radius: float):
        return CalculateAreaFigures.pi * radius ** 2

