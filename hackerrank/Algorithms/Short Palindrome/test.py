import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.shortPalindrome('kkkkkkz'), 15)

    def test_case_1(self):
        self.assertEqual(solution.shortPalindrome('abbaab'), 4)

    def test_case_2(self):
        self.assertEqual(solution.shortPalindrome('akakak'), 2)


if __name__ == '__main__':
    unittest.main()
