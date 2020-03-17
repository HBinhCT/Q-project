import unittest
import my_code


class TestCaesarCipher(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.caesarCipher('middle-Outz', 2), 'okffng-Qwvb')

    def test_case_1(self):
        self.assertEqual(
            my_code.caesarCipher('Always-Look-on-the-Bright-Side-of-Life', 5),
            'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj'
        )


if __name__ == '__main__':
    unittest.main()
