import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.funnyString('acxz'), 'Funny')
        self.assertEqual(solution.funnyString('bcxz'), 'Not Funny')

    def test_case_1(self):
        self.assertEqual(solution.funnyString('ivvkxq'), 'Not Funny')
        self.assertEqual(solution.funnyString('ivvkx'), 'Not Funny')


if __name__ == '__main__':
    unittest.main()
