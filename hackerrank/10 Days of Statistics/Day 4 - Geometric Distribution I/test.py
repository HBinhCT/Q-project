import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(round(solution.geometric_distribution(5, 1 / 3), 3), 0.066)


if __name__ == '__main__':
    unittest.main()
