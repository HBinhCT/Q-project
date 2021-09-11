import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.solve([5, 4, 3, 4, 5]), 8)


if __name__ == '__main__':
    unittest.main()
