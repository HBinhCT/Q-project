import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.larrysArray([3, 1, 2]), 'YES')
        self.assertEqual(my_code.larrysArray([1, 3, 4, 2]), 'YES')
        self.assertEqual(my_code.larrysArray([1, 2, 3, 5, 4]), 'NO')

    def test_case_1(self):
        self.assertEqual(my_code.larrysArray([1, 6, 5, 2, 3, 4]), 'NO')
        self.assertEqual(my_code.larrysArray([3, 1, 2, 4]), 'YES')


if __name__ == '__main__':
    unittest.main()
