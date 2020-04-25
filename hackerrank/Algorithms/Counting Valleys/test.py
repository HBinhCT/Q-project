import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.countingValleys(8, 'UDDDUDUU'), 1)

    def test_case_1(self):
        self.assertEqual(my_code.countingValleys(12, 'DDUUDDUDUUUD'), 2)


if __name__ == '__main__':
    unittest.main()
