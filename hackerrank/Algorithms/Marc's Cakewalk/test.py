import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.marcsCakewalk([1, 3, 2]), 11)

    def test_case_1(self):
        self.assertEqual(solution.marcsCakewalk([7, 4, 9, 6]), 79)


if __name__ == '__main__':
    unittest.main()
