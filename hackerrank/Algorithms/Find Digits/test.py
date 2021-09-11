import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.findDigits(12), 2)
        self.assertEqual(solution.findDigits(1012), 3)


if __name__ == '__main__':
    unittest.main()
