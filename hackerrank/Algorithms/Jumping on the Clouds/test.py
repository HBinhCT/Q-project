import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]), 4)

    def test_case_1(self):
        self.assertEqual(my_code.jumpingOnClouds([0, 0, 0, 1, 0, 0]), 3)


if __name__ == '__main__':
    unittest.main()