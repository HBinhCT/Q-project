import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.sherlockAndAnagrams('abba'), 4)
        self.assertEqual(my_code.sherlockAndAnagrams('abcd'), 0)

    def test_case_1(self):
        self.assertEqual(my_code.sherlockAndAnagrams('ifailuhkqq'), 3)
        self.assertEqual(my_code.sherlockAndAnagrams('kkkk'), 10)

    def test_case_2(self):
        self.assertEqual(my_code.sherlockAndAnagrams('cdcd'), 5)


if __name__ == '__main__':
    unittest.main()
