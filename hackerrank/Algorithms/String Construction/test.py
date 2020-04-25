import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.stringConstruction('abcd'), 4)
        self.assertEqual(my_code.stringConstruction('abab'), 2)

    def test_case_1(self):
        self.assertEqual(my_code.stringConstruction('scfg'), 4)
        self.assertEqual(my_code.stringConstruction('bccb'), 2)


if __name__ == '__main__':
    unittest.main()
