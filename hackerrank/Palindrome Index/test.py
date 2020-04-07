import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.palindromeIndex('aaab'), 3)
        self.assertEqual(my_code.palindromeIndex('baa'), 0)
        self.assertEqual(my_code.palindromeIndex('aaa'), -1)


if __name__ == '__main__':
    unittest.main()
