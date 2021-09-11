import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]), 169.375)


if __name__ == '__main__':
    unittest.main()
