import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.isBalanced('{[()]}'), 'YES')
        self.assertEqual(solution.isBalanced('{[(])}'), 'NO')
        self.assertEqual(solution.isBalanced('{{[[(())]]}}'), 'YES')

    def test_case_1(self):
        self.assertEqual(solution.isBalanced('{{([])}}'), 'YES')
        self.assertEqual(solution.isBalanced('{{)[](}}'), 'NO')

    def test_case_2(self):
        self.assertEqual(solution.isBalanced('{(([])[])[]}'), 'YES')
        self.assertEqual(solution.isBalanced('{(([])[])[]]}'), 'NO')
        self.assertEqual(solution.isBalanced('{(([])[])[]}[]'), 'YES')


if __name__ == '__main__':
    unittest.main()
