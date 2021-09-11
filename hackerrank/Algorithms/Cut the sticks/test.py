import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(list(solution.cutTheSticks([5, 4, 4, 2, 2, 8])), [6, 4, 2, 1])

    def test_case_1(self):
        self.assertEqual(list(solution.cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1])), [8, 6, 4, 1])


if __name__ == '__main__':
    unittest.main()
