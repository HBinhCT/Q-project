import math
import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        a = solution.Points(0, 4, 5)
        b = solution.Points(1, 7, 6)
        c = solution.Points(0, 5, 9)
        d = solution.Points(1, 7, 2)
        x = (b - a).cross(c - b)
        y = (c - b).cross(d - c)
        angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
        self.assertEqual(f'{math.degrees(angle):.2f}', '8.19')

    def test_case_1(self):
        a = solution.Points(5, 8.8, 9)
        b = solution.Points(4, -1, 3)
        c = solution.Points(7, 8.7, 3.3)
        d = solution.Points(4.4, 5.1, 6.3)
        x = (b - a).cross(c - b)
        y = (c - b).cross(d - c)
        angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
        self.assertEqual(f'{math.degrees(angle):.2f}', '5.69')


if __name__ == '__main__':
    unittest.main()
