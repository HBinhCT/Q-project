import unittest
import my_code


class TestCaesarCipher(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.camelcase('saveChangesInTheEditor'), 5)


if __name__ == '__main__':
    unittest.main()
