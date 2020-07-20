import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.prims(
            5,
            [
                [1, 2, 3],
                [1, 3, 4],
                [4, 2, 6],
                [5, 2, 2],
                [2, 3, 5],
                [3, 5, 7],
            ],
            1,
        ), 15)


if __name__ == '__main__':
    unittest.main()
