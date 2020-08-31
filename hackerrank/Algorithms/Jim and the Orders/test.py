import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.jimOrders([[1, 3], [2, 3], [3, 3]]), [1, 2, 3])

    def test_case_1(self):
        self.assertEqual(solution.jimOrders([[8, 1], [4, 2], [5, 6], [3, 1], [4, 3]]), [4, 2, 5, 1, 3])


if __name__ == '__main__':
    unittest.main()
