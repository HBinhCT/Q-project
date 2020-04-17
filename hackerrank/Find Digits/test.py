import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.findDigits(12), 2)
        self.assertEqual(my_code.findDigits(1012), 3)


if __name__ == '__main__':
    unittest.main()
