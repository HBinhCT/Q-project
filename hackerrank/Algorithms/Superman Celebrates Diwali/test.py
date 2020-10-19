import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.solve(
            4,
            15,
            2,
            [
                [5, 1, 1, 1, 4, 10],
                [8, 3, 5, 7, 7, 8, 8, 9, 9],
                [5, 3, 4, 5, 6, 9],
                [0]
            ]
        ), 12)


if __name__ == '__main__':
    unittest.main()
