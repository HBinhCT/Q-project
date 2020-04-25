import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.getTotalX([2, 4], [16, 32, 96]), 3)

    def test_case_1(self):
        self.assertEqual(my_code.getTotalX([3, 4], [24, 48]), 2)


if __name__ == '__main__':
    unittest.main()
