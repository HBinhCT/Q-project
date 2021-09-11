import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.marsExploration('SOSSPSSQSSOR'), 3)

    def test_case_1(self):
        self.assertEqual(solution.marsExploration('SOSSOT'), 1)

    def test_case_2(self):
        self.assertEqual(solution.marsExploration('SOSSOSSOS'), 0)


if __name__ == '__main__':
    unittest.main()
