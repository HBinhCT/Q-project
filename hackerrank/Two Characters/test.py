import unittest
import my_code


class TestCaesarCipher(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(my_code.alternate('beabeefeab'), 5)

    def test_case_two(self):
        self.assertEqual(my_code.alternate('asdcbsdcagfsdbgdfanfghbsfdab'), 8)

    def test_case_three(self):
        self.assertEqual(my_code.alternate('asvkugfiugsalddlasguifgukvsa'), 0)


if __name__ == '__main__':
    unittest.main()
