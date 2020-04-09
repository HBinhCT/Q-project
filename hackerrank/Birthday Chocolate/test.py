import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.birthday([1, 2, 1, 3, 2], 3, 2), 2)

    def test_case_1(self):
        self.assertEqual(my_code.birthday([1, 1, 1, 1, 1, 1], 3, 2), 0)

    def test_case_2(self):
        self.assertEqual(my_code.birthday([4], 4, 1), 1)


if __name__ == '__main__':
    unittest.main()
