import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.cipher(4, '1110100110'), '1001010')

    def test_case_1(self):
        self.assertEqual(solution.cipher(2, '1110001'), '101111')

    def test_case_2(self):
        self.assertEqual(solution.cipher(3, '1110011011'), '10000101')


if __name__ == '__main__':
    unittest.main()
