import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        dist = solution.calculate_distances(5,
                                            [1, 1, 1, 1, 2, 3, 4],
                                            [2, 3, 4, 5, 3, 4, 5],
                                            [20, 50, 70, 90, 30, 40, 60])
        self.assertEqual(solution.shortest_distance(dist, 1, 4), 70)
        self.assertEqual(solution.shortest_distance(dist, 5, 1), -1)
        self.assertEqual(solution.shortest_distance(dist, 2, 5), 130)
        self.assertEqual(solution.shortest_distance(dist, 3, 4), 40)
        self.assertEqual(solution.shortest_distance(dist, 1, 4), 70)
        self.assertEqual(solution.shortest_distance(dist, 1, 2), 20)
        self.assertEqual(solution.shortest_distance(dist, 3, 1), -1)
        self.assertEqual(solution.shortest_distance(dist, 1, 2), 20)

    def test_case_1(self):
        dist = solution.calculate_distances(4,
                                            [1, 1, 2, 3, 3],
                                            [2, 4, 4, 4, 2],
                                            [5, 24, 6, 4, 7])
        self.assertEqual(solution.shortest_distance(dist, 1, 2), 5)
        self.assertEqual(solution.shortest_distance(dist, 3, 1), -1)
        self.assertEqual(solution.shortest_distance(dist, 1, 4), 11)


if __name__ == '__main__':
    unittest.main()
