import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.equalizeArray([3, 3, 2, 1, 3]), 2)

    def test_case_1(self):
        self.assertEqual(my_code.equalizeArray([1, 2, 3, 1, 2, 3, 3, 3]), 4)


if __name__ == '__main__':
    unittest.main()
