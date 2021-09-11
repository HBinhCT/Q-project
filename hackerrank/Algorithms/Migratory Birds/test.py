import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.migratoryBirds([1, 4, 4, 4, 5, 3]), 4)

    def test_case_1(self):
        self.assertEqual(solution.migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]), 3)


if __name__ == '__main__':
    unittest.main()
