import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.pickingNumbers([4, 6, 5, 3, 3, 1]), 3)

    def test_case_1(self):
        self.assertEqual(my_code.pickingNumbers([1, 2, 2, 3, 1, 2]), 5)


if __name__ == '__main__':
    unittest.main()
