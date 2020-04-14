import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(
            my_code.climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]),
            [6, 4, 2, 1]
        )

    def test_case_1(self):
        self.assertEqual(
            my_code.climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]),
            [6, 5, 4, 2, 1]
        )


if __name__ == '__main__':
    unittest.main()
