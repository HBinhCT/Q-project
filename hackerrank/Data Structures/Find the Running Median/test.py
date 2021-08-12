import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertListEqual(
            solution.runningMedian([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
        )


if __name__ == '__main__':
    unittest.main()
