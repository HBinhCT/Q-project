import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.getMoneySpent([3, 1], [5, 2, 8], 10), 9)

    def test_case_1(self):
        self.assertEqual(my_code.getMoneySpent([4], [5], 5), -1)


if __name__ == '__main__':
    unittest.main()
