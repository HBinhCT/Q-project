import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]), 5000000015)


if __name__ == '__main__':
    unittest.main()
