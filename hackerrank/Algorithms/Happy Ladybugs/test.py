import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.happyLadybugs('RBY_YBR'), 'YES')
        self.assertEqual(solution.happyLadybugs('X_Y__X'), 'NO')
        self.assertEqual(solution.happyLadybugs('__'), 'YES')
        self.assertEqual(solution.happyLadybugs('B_RRBR'), 'YES')

    def test_case_1(self):
        self.assertEqual(solution.happyLadybugs('AABBC'), 'NO')
        self.assertEqual(solution.happyLadybugs('AABBC_C'), 'YES')
        self.assertEqual(solution.happyLadybugs('_'), 'YES')
        self.assertEqual(solution.happyLadybugs('DD__FQ_QQF'), 'YES')
        self.assertEqual(solution.happyLadybugs('AABCBC'), 'NO')


if __name__ == '__main__':
    unittest.main()
