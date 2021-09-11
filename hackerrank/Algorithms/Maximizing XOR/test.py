import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.maximizingXor(10, 15), 7)

    def test_case_1(self):
        self.assertEqual(solution.maximizingXor(11, 100), 127)


if __name__ == '__main__':
    unittest.main()
