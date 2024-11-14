import unittest

def area(a, h):
	return a * h / 2
	'''Принимает a и h, возвращает площадь триугольника с высотой h и основанием a
		Например:
        	area(5, 4)
       		10
	'''

def perimeter(a, b, c):
	return a + b + c
	'''Принимает a, b, c и возвращает периметр триугольника со сторонами a, b, c
		Например:
        	perimeter(5, 3, 6)
        	21
	'''
      
class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        res = area(10, 4)
        self.assertEqual(res, 20)
        

    def test_perimeter(self):
        res = perimeter(10, 30, 45)
        self.assertEqual(res, 85)
