import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.birthdayCakeCandles([3, 2, 1, 3]), 2)


if __name__ == '__main__':
    unittest.main()
