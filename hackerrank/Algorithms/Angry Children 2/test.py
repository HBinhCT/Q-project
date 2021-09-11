import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.angryChildren(3, [10, 100, 300, 200, 1000, 20, 30]), 40)

    def test_case_1(self):
        self.assertEqual(solution.angryChildren(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]), 10)


if __name__ == '__main__':
    unittest.main()
