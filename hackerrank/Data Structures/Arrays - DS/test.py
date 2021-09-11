import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertListEqual(solution.reverseArray([1, 4, 3, 2]), [2, 3, 4, 1])


if __name__ == '__main__':
    unittest.main()
