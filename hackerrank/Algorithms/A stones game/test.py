import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.half(1), 1)
        self.assertEqual(solution.half(10), 7)
        self.assertEqual(solution.half(6), 2)
        self.assertEqual(solution.half(8), 7)
        self.assertEqual(solution.half(123456), 32768)

    def test_case_1(self):
        self.assertEqual(solution.half(3), 1)


if __name__ == '__main__':
    unittest.main()
