import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.flatlandSpaceStations(5, [0, 4]), 2)

    def test_case_1(self):
        self.assertEqual(solution.flatlandSpaceStations(6, [0, 1, 2, 4, 3, 5]), 0)


if __name__ == '__main__':
    unittest.main()
