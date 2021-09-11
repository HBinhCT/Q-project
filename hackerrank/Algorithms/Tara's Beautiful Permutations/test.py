import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.beautifulPermutations([1, 1, 2]), 1)
        self.assertEqual(solution.beautifulPermutations([1, 2]), 2)
        self.assertEqual(solution.beautifulPermutations([1, 2, 2, 1]), 2)


if __name__ == '__main__':
    unittest.main()
