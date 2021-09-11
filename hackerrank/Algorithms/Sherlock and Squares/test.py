import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.squares(3, 9), 2)
        self.assertEqual(solution.squares(17, 24), 0)

    def test_case_1(self):
        self.assertEqual(solution.squares(35, 70), 3)
        self.assertEqual(solution.squares(100, 1000), 22)


if __name__ == '__main__':
    unittest.main()
