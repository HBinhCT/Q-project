import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.travelAroundTheWorld([3, 3, 0], [2, 2, 2], 2), 0)

    def test_case_1(self):
        self.assertEqual(solution.travelAroundTheWorld([3, 1, 2], [2, 2, 2], 3), 2)

    def test_case_2(self):
        self.assertEqual(solution.travelAroundTheWorld([3, 1, 2], [2, 2, 2], 2), 0)


if __name__ == '__main__':
    unittest.main()
