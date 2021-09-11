import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.sumXor(5), 2)

    def test_case_1(self):
        self.assertEqual(solution.sumXor(10), 4)


if __name__ == '__main__':
    unittest.main()
