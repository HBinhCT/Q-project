import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.dayOfProgrammer(2017), '13.09.2017')

    def test_case_1(self):
        self.assertEqual(solution.dayOfProgrammer(2016), '12.09.2016')

    def test_case_2(self):
        self.assertEqual(solution.dayOfProgrammer(1800), '12.09.1800')


if __name__ == '__main__':
    unittest.main()
