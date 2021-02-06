import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.isWinning(4, 'IXXI'), 'LOSE')
        self.assertEqual(solution.isWinning(4, 'XIIX'), 'WIN')
        self.assertEqual(solution.isWinning(5, 'IIXII'), 'LOSE')
        self.assertEqual(solution.isWinning(5, 'IIIII'), 'WIN')


if __name__ == '__main__':
    unittest.main()
