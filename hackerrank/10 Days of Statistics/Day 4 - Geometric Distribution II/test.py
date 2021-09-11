import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        result = sum(solution.geometric_distribution(i, 1 / 3) for i in range(1, 6))
        self.assertEqual(round(result, 3), 0.868)


if __name__ == '__main__':
    unittest.main()
