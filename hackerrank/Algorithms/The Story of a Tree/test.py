import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.storyOfATree(
            4,
            [
                [1, 2],
                [1, 3],
                [3, 4],
            ],
            2,
            [
                (1, 2),
                (3, 4),
            ]
        ), '1/2')
        self.assertEqual(solution.storyOfATree(
            3,
            [
                [1, 2],
                [1, 3],
            ],
            2,
            [
                (1, 2),
                (1, 3),
            ]
        ), '1/3')


if __name__ == '__main__':
    unittest.main()
