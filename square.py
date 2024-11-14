import unittest

def area(a):
    return a * a
    '''Приниает a возводит в квадрат, возвращает площадь
        Например:
            area(5)
            25
    '''
            
def perimeter(a):
    return 4 * a
    '''принимает a и возвращает его периметр квадрата со стороной a
        Например:
            perimeter(5)
            20
    '''

class SquareTestCase(unittest.TestCase):

    def test_area(self):
        res = area(10)
        self.assertEqual(res, 100)
        

    def test_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
