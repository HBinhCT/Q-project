import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertListEqual(solution.waiter([3, 4, 7, 6, 5], 1), [4, 6, 3, 7, 5])

    def test_case_1(self):
        self.assertListEqual(solution.waiter([3, 3, 4, 4, 9], 2), [4, 4, 9, 3, 3])


if __name__ == '__main__':
    unittest.main()
