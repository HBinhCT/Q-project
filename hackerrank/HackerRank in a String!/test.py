import unittest
import my_code


class TestCaesarCipher(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.hackerrankInString('hackerrankInString'), 'YES')
        self.assertEqual(my_code.hackerrankInString('hackerworld'), 'NO')

    def test_case_1(self):
        self.assertEqual(my_code.hackerrankInString('hhaacckkekraraannk'), 'YES')
        self.assertEqual(my_code.hackerrankInString('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'), 'NO')


if __name__ == '__main__':
    unittest.main()
