
"""  
Задача 1. Создать класс для вычисления площади 
геометрических фигур: квадрат, прямоугольник, круг

"""


class CalculateAreaFigures:
    from math import pi

    @staticmethod
    def area_square(side: float):
        return side ** 2

    @staticmethod
    def area_rectangle(side_a: float, side_b: float):
        return side_a * side_b

    @staticmethod
    def area_circle(radius: float):
        return CalculateAreaFigures.pi * radius ** 2

