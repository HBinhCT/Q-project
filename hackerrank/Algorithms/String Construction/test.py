import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.stringConstruction('abcd'), 4)
        self.assertEqual(solution.stringConstruction('abab'), 2)

    def test_case_1(self):
        self.assertEqual(solution.stringConstruction('scfg'), 4)
        self.assertEqual(solution.stringConstruction('bccb'), 2)


if __name__ == '__main__':
    unittest.main()
