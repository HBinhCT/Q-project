import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.saveThePrisoner(5, 2, 1), 2)
        self.assertEqual(solution.saveThePrisoner(5, 2, 2), 3)

    def test_case_1(self):
        self.assertEqual(solution.saveThePrisoner(7, 19, 2), 6)
        self.assertEqual(solution.saveThePrisoner(3, 7, 3), 3)


if __name__ == '__main__':
    unittest.main()
