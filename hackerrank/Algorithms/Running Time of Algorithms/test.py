import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.runningTime([2, 1, 3, 1, 2]), 4)

    def test_case_1(self):
        self.assertEqual(my_code.runningTime([1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 9, 9]), 0)


if __name__ == '__main__':
    unittest.main()
