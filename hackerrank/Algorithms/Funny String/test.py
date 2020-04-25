import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.funnyString('acxz'), 'Funny')
        self.assertEqual(my_code.funnyString('bcxz'), 'Not Funny')

    def test_case_1(self):
        self.assertEqual(my_code.funnyString('ivvkxq'), 'Not Funny')
        self.assertEqual(my_code.funnyString('ivvkx'), 'Not Funny')


if __name__ == '__main__':
    unittest.main()
