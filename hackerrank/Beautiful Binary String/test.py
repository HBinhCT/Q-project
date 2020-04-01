import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.beautifulBinaryString('0101010'), 2)

    def test_case_1(self):
        self.assertEqual(my_code.beautifulBinaryString('01100'), 0)

    def test_case_2(self):
        self.assertEqual(my_code.beautifulBinaryString('0100101010'), 3)


if __name__ == '__main__':
    unittest.main()
