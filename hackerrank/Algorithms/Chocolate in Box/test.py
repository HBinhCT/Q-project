import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.chocolateInBox([2, 3]), 1)


if __name__ == '__main__':
    unittest.main()
