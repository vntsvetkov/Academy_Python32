# test.py

import unittest
from main import CalculateAreaFigures

"""
class TestCalculateAreaFigures:

    @staticmethod
    def test_area_square():
        assert CalculateAreaFigures.area_square(3) == 9, f"Неверный расчет площади со стороной 3"
        assert CalculateAreaFigures.area_square(-1) == 0, f"Неверный расчет площади со стороной -1"
        assert CalculateAreaFigures.area_square(1.5) == 2.25, f"Неверный расчет площади со стороной 1.5"
        assert CalculateAreaFigures.area_square('t') == None, f"Неверный расчет площади со значением 't'"
        print("ОК")

"""


class TestCalculateAreaFigures(unittest.TestCase):

    def test_area_square(self):
        self.assertEqual(CalculateAreaFigures.area_square(2), 4)
        self.assertEqual(CalculateAreaFigures.area_square(1.5), 2.25)
        self.assertRaises(ValueError, CalculateAreaFigures.area_square, -1)
        self.assertRaises(TypeError, CalculateAreaFigures.area_square, "")
        self.assertRaises(TypeError, CalculateAreaFigures.area_square, None)

    def test_area_rectangle(self):
        self.assertEqual(CalculateAreaFigures.area_rectangle(1, 2), 2)
        self.assertEqual(CalculateAreaFigures.area_rectangle(1, 1.5), 1.5)

    def test_area_circle(self):
        self.assertEqual(round(CalculateAreaFigures.area_circle(1), 2), 3.14)
        self.assertEqual(round(CalculateAreaFigures.area_circle(1.5), 2), 7.07)


if __name__ == '__main__':
    unittest.main()

