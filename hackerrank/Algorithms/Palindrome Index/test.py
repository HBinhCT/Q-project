import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.palindromeIndex('aaab'), 3)
        self.assertEqual(solution.palindromeIndex('baa'), 0)
        self.assertEqual(solution.palindromeIndex('aaa'), -1)


if __name__ == '__main__':
    unittest.main()
