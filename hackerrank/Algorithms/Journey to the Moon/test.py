import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.journeyToMoon(5, [[0, 1], [2, 3], [0, 4]]), 6)

    def test_case_1(self):
        self.assertEqual(solution.journeyToMoon(4, [[0, 2]]), 5)


if __name__ == '__main__':
    unittest.main()
