import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.hackerrankInString('hackerrankInString'), 'YES')
        self.assertEqual(solution.hackerrankInString('hackerworld'), 'NO')

    def test_case_1(self):
        self.assertEqual(solution.hackerrankInString('hhaacckkekraraannk'), 'YES')
        self.assertEqual(solution.hackerrankInString('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'), 'NO')


if __name__ == '__main__':
    unittest.main()
