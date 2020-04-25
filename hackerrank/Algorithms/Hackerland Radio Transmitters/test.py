import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.hackerlandRadioTransmitters([1, 2, 3, 4, 5], 1), 2)

    def test_case_1(self):
        self.assertEqual(my_code.hackerlandRadioTransmitters([7, 2, 4, 6, 5, 9, 12, 11], 2), 3)


if __name__ == '__main__':
    unittest.main()
