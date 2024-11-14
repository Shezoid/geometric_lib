import math
import unittest
import math

def area(r):
    return math.pi * r * r
    '''Принимает r, возводит в квадрат и домножает на pi, возвращает площадь круга
        Например:
        area(5)
        78,539816339744830
    '''

def perimeter(r):
    return 2 * math.pi * r
    '''Принимает r, возвращает длину окружности
        Например:
            perimeter(5)
            31,415926535897932
    '''


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        res = area(2)
        self.assertEqual(res, math.pi * 2 * 2)

    def test_perimeter(self):
        res = area(2)
        self.assertEqual(res, 2 * math.pi * 2)
