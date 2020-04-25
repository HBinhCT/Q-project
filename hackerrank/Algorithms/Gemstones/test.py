import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.gemstones(['abcdde', 'baccd', 'eeabg']), 2)

    def test_case_1(self):
        self.assertEqual(my_code.gemstones(['basdfj', 'asdlkjfdjsa', 'bnafvfnsd', 'oafhdlasd']), 4)

    def test_case_2(self):
        self.assertEqual(my_code.gemstones(['vtrjvgbj', 'mkmjyaeav', 'sibzdmsk']), 0)


if __name__ == '__main__':
    unittest.main()
