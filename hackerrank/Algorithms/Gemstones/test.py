import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.gemstones(['abcdde', 'baccd', 'eeabg']), 2)

    def test_case_1(self):
        self.assertEqual(solution.gemstones(['basdfj', 'asdlkjfdjsa', 'bnafvfnsd', 'oafhdlasd']), 4)

    def test_case_2(self):
        self.assertEqual(solution.gemstones(['vtrjvgbj', 'mkmjyaeav', 'sibzdmsk']), 0)


if __name__ == '__main__':
    unittest.main()
