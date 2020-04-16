import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.beautifulDays(20, 23, 6), 2)

    def test_case_1(self):
        self.assertEqual(my_code.beautifulDays(13, 45, 3), 33)


if __name__ == '__main__':
    unittest.main()
