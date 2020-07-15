import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.evenForest(
            10,
            9,
            [2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 1, 3, 2, 1, 2, 6, 8, 8],
        ), 2)


if __name__ == '__main__':
    unittest.main()
