import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.maximumPerimeterTriangle([1, 1, 1, 3, 3]), [1, 3, 3])

    def test_case_1(self):
        self.assertEqual(solution.maximumPerimeterTriangle([1, 2, 3]), [-1])

    def test_case_2(self):
        self.assertEqual(solution.maximumPerimeterTriangle([1, 1, 1, 2, 3, 5]), [1, 1, 1])


if __name__ == '__main__':
    unittest.main()
