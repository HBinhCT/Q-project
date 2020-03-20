import unittest
import my_code


class TestCaesarCipher(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.quickSort([4, 5, 3, 7, 2]), [3, 2, 4, 5, 7])


if __name__ == '__main__':
    unittest.main()
