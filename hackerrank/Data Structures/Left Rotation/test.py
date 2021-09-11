import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertListEqual(solution.rotateLeft(4, [1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
