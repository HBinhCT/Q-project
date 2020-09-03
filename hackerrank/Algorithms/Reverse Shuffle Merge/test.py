import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.reverseShuffleMerge('eggegg'), 'egg')

    def test_case_1(self):
        self.assertEqual(solution.reverseShuffleMerge('abcdefgabcdefg'), 'agfedcb')

    def test_case_2(self):
        self.assertEqual(solution.reverseShuffleMerge('aeiouuoiea'), 'aeiou')


if __name__ == '__main__':
    unittest.main()
