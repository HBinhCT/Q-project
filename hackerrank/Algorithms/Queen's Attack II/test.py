import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.queensAttack(4, 0, 4, 4, []), 9)

    def test_case_1(self):
        self.assertEqual(solution.queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]), 10)

    def test_case_2(self):
        self.assertEqual(solution.queensAttack(1, 0, 1, 1, []), 0)


if __name__ == '__main__':
    unittest.main()
