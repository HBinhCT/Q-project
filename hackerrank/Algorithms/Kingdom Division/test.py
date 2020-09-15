import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.kingdomDivision(5, [
            [1, 2],
            [1, 3],
            [3, 4],
            [3, 5],
        ]), 4)

    def test_case_1(self):
        self.assertEqual(solution.kingdomDivision(7, [
            [1, 2],
            [1, 5],
            [2, 3],
            [2, 4],
            [5, 6],
            [7, 5],
        ]), 6)


if __name__ == '__main__':
    unittest.main()
