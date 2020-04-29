import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.howManyGames(20, 3, 6, 80), 6)

    def test_case_1(self):
        self.assertEqual(solution.howManyGames(20, 3, 6, 85), 7)


if __name__ == '__main__':
    unittest.main()
