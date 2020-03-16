import unittest
import my_code


class TestCaesarCipher(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(my_code.minimumNumber(3, 'Ab1'), 3)

    def test_case_two(self):
        self.assertEqual(my_code.minimumNumber(11, '#HackerRank'), 1)


if __name__ == '__main__':
    unittest.main()
