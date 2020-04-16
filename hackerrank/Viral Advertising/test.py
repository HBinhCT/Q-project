import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.viralAdvertising(3), 9)

    def test_case_1(self):
        self.assertEqual(my_code.viralAdvertising(4), 15)


if __name__ == '__main__':
    unittest.main()
