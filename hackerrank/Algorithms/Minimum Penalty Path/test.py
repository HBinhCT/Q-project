import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(
            solution.beautifulPath(
                3,
                [
                    [1, 2, 1],
                    [1, 2, 1000],
                    [2, 3, 3],
                    [1, 3, 100]
                ],
                1,
                3),
            3)


if __name__ == '__main__':
    unittest.main()
