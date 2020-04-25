import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.saveThePrisoner(5, 2, 1), 2)
        self.assertEqual(my_code.saveThePrisoner(5, 2, 2), 3)

    def test_case_1(self):
        self.assertEqual(my_code.saveThePrisoner(7, 19, 2), 6)
        self.assertEqual(my_code.saveThePrisoner(3, 7, 3), 3)


if __name__ == '__main__':
    unittest.main()
