import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.xorMatrix(2, [6, 7, 1, 3]), [1, 6, 2, 5])


if __name__ == '__main__':
    unittest.main()
