import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.gridlandMetro(4, 4, 3, [[2, 2, 3], [3, 1, 4], [4, 4, 4]]), 9)

    def test_case_1(self):
        self.assertEqual(solution.gridlandMetro(4, 4, 0, []), 16)


if __name__ == '__main__':
    unittest.main()
