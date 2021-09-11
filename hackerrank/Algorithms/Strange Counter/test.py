import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.strangeCounter(4), 6)

    def test_case_1(self):
        self.assertEqual(solution.strangeCounter(17), 5)


if __name__ == '__main__':
    unittest.main()
