import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.findMedian([0, 1, 2, 4, 6, 5, 3]), 3)


if __name__ == '__main__':
    unittest.main()
