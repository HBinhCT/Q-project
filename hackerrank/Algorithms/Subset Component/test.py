import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.findConnectedComponents([2, 5, 9]), 504)


if __name__ == '__main__':
    unittest.main()
