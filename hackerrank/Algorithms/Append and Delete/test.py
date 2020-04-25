import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.appendAndDelete('hackerhappy', 'hackerrank', 9), 'Yes')

    def test_case_1(self):
        self.assertEqual(my_code.appendAndDelete('aba', 'aba', 7), 'Yes')

    def test_case_2(self):
        self.assertEqual(my_code.appendAndDelete('ashley', 'ash', 2), 'No')


if __name__ == '__main__':
    unittest.main()
