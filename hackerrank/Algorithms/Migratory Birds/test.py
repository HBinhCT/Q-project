import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.migratoryBirds([1, 4, 4, 4, 5, 3]), 4)

    def test_case_1(self):
        self.assertEqual(my_code.migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]), 3)


if __name__ == '__main__':
    unittest.main()
