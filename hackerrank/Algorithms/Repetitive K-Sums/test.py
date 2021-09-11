import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.repetitive_k_sums(3, [3]), [1])
        self.assertEqual(solution.repetitive_k_sums(2, [12, 34, 56]), [6, 28])
        self.assertEqual(solution.repetitive_k_sums(2, [2, 3, 4, 4, 5, 6]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
