import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.extremumPermutations(4, [2], [3]), 5)

    def test_case_1(self):
        self.assertEqual(solution.extremumPermutations(10, [2, 4], [3, 9]), 161280)


if __name__ == '__main__':
    unittest.main()
