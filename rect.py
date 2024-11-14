import unittest

def area(a, b):
	return a * b
	'''Приниает a и b,возвращает площадь прямоугольника со сторонами a и b
		Например:
        	area(5, 9)
        	45
	'''

def perimeter(a, b):
	return 2 * (a + b)	
	'''Принимает a и b, возвращает периметр прямоугольника со стронами a и b
		Например:
        	perimeter(5, 9)
        	28
	'''

class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        res = area(10, 25)
        self.assertEqual(res, 250)
        
    def test_perimeter(self):
        res = perimeter(10, 25)
        self.assertEqual(res, 70)
        