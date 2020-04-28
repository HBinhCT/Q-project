import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.chocolateFeast(10, 2, 5), 6)
        self.assertEqual(my_code.chocolateFeast(12, 4, 4), 3)
        self.assertEqual(my_code.chocolateFeast(6, 2, 2), 5)

    def test_case_1(self):
        self.assertEqual(my_code.chocolateFeast(7, 3, 2), 3)


if __name__ == '__main__':
    unittest.main()
