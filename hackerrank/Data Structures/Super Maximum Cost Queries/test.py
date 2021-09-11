import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertListEqual(
            list(solution.solve(
                [
                    [1, 2, 3],
                    [1, 4, 2],
                    [2, 5, 6],
                    [3, 4, 1],
                ],
                [
                    [1, 1],
                    [1, 2],
                    [2, 3],
                    [2, 5],
                    [1, 6],
                ],
            )),
            [1, 3, 5, 5, 10],
        )


if __name__ == '__main__':
    unittest.main()
