import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]), [2, 4])

    def test_case_1(self):
        self.assertEqual(my_code.breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]), [4, 0])


if __name__ == '__main__':
    unittest.main()
