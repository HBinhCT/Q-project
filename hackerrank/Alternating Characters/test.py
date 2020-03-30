import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.alternatingCharacters('AAAA'), 3)
        self.assertEqual(my_code.alternatingCharacters('BBBBB'), 4)
        self.assertEqual(my_code.alternatingCharacters('ABABABAB'), 0)
        self.assertEqual(my_code.alternatingCharacters('BABABA'), 0)
        self.assertEqual(my_code.alternatingCharacters('AAABBB'), 4)

    def test_case_1(self):
        self.assertEqual(my_code.alternatingCharacters('AAABBBAABB'), 6)
        self.assertEqual(my_code.alternatingCharacters('AABBAABB'), 4)
        self.assertEqual(my_code.alternatingCharacters('ABABABAA'), 1)

    def test_case_2(self):
        self.assertEqual(my_code.alternatingCharacters('ABBABBAA'), 3)


if __name__ == '__main__':
    unittest.main()
