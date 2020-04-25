import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.taumBday(10, 10, 1, 1, 1), 20)
        self.assertEqual(my_code.taumBday(5, 9, 2, 3, 4), 37)
        self.assertEqual(my_code.taumBday(3, 6, 9, 1, 1), 12)
        self.assertEqual(my_code.taumBday(7, 7, 4, 2, 1), 35)
        self.assertEqual(my_code.taumBday(3, 3, 1, 9, 2), 12)

    def test_case_1(self):
        self.assertEqual(my_code.taumBday(3, 5, 3, 4, 1), 29)


if __name__ == '__main__':
    unittest.main()
