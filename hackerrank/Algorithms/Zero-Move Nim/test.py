import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.zeroMoveNim([1, 2]), 'W')
        self.assertEqual(solution.zeroMoveNim([2, 2]), 'L')


if __name__ == '__main__':
    unittest.main()
