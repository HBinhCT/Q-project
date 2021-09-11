import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.chocolateGame([1, 1, 2, 2, 3]), 5)


if __name__ == '__main__':
    unittest.main()
