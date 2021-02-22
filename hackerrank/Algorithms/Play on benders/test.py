import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(
            solution.bendersPlay(
                10,
                [
                    [1, 10],
                    [3, 10],
                    [7, 8],
                    [6, 8],
                    [7, 4],
                    [9, 4],
                    [7, 6],
                    [5, 8],
                    [1, 8],
                    [2, 8],
                ],
                [
                    [10, 7, 6, 4],
                    [1, 9, 4],
                    [8, 3, 5],
                    [4, 9, 7],
                    [7, 9, 10],
                ]
            ),
            [
                'Bumi',
                'Iroh',
                'Iroh',
                'Bumi',
                'Bumi',
            ]
        )


if __name__ == '__main__':
    unittest.main()
