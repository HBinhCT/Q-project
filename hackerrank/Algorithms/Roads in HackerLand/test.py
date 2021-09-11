import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.roadsInHackerland(5, [
            [1, 3, 5],
            [4, 5, 0],
            [2, 1, 3],
            [3, 2, 1],
            [4, 3, 4],
            [4, 2, 2],
        ]), '1000100')


if __name__ == '__main__':
    unittest.main()
