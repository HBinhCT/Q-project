import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.insertionSort([1, 1, 1, 2, 2]), 0)
        self.assertEqual(solution.insertionSort([2, 1, 3, 1, 2]), 4)

    def test_case_1(self):
        self.assertEqual(solution.insertionSort([12, 15, 1, 5, 6, 14, 11]), 10)
        self.assertEqual(solution.insertionSort([3, 5, 7, 11, 9]), 1)


if __name__ == '__main__':
    unittest.main()
