import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.sherlockAndAnagrams('abba'), 4)
        self.assertEqual(solution.sherlockAndAnagrams('abcd'), 0)

    def test_case_1(self):
        self.assertEqual(solution.sherlockAndAnagrams('ifailuhkqq'), 3)
        self.assertEqual(solution.sherlockAndAnagrams('kkkk'), 10)

    def test_case_2(self):
        self.assertEqual(solution.sherlockAndAnagrams('cdcd'), 5)


if __name__ == '__main__':
    unittest.main()
