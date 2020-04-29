import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5), 2)

    def test_case_1(self):
        self.assertEqual(solution.activityNotifications([1, 2, 3, 4, 4], 4), 0)

    def test_case_2(self):
        self.assertEqual(solution.activityNotifications([10, 20, 30, 40, 50], 3), 1)


if __name__ == '__main__':
    unittest.main()
