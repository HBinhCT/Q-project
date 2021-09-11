import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertListEqual(solution.dynamicArray(
            2,
            [
                [1, 0, 5],
                [1, 1, 7],
                [1, 0, 3],
                [2, 1, 0],
                [2, 1, 1],
            ],
        ), [7, 3])


if __name__ == '__main__':
    unittest.main()
