import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.icecreamParlor(4, [1, 4, 5, 3, 2]), (1, 4))
        self.assertEqual(my_code.icecreamParlor(4, [2, 2, 4, 3]), (1, 2))

    def test_case_1(self):
        self.assertEqual(my_code.icecreamParlor(9, [1, 3, 4, 6, 7, 9]), (2, 4))
        self.assertEqual(my_code.icecreamParlor(8, [1, 3, 4, 4, 6, 8]), (3, 4))
        self.assertEqual(my_code.icecreamParlor(3, [1, 2]), (1, 2))


if __name__ == '__main__':
    unittest.main()
