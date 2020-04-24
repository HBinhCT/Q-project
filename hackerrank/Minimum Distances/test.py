import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.minimumDistances([7, 1, 3, 4, 1, 7]), 3)

    def test_case_1(self):
        self.assertEqual(my_code.minimumDistances([1, 2, 3, 4, 10]), -1)


if __name__ == '__main__':
    unittest.main()
