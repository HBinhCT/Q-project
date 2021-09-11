import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.specialSubCubes(2, [2, 1, 1, 1, 1, 1, 1, 1]), [7, 1])

    def test_case_1(self):
        self.assertEqual(solution.specialSubCubes(2, [1, 1, 1, 1, 2, 1, 1, 2]), [6, 1])


if __name__ == '__main__':
    unittest.main()
