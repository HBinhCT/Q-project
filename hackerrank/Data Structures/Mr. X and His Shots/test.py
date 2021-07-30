import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.solve(
            [
                [1, 2],
                [2, 3],
                [4, 5],
                [6, 7],
            ],
            [
                [1, 5],
                [2, 3],
                [4, 7],
                [5, 7],
            ]
        ), 9)


if __name__ == '__main__':
    unittest.main()
