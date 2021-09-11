import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.beadOrnaments([2, 1]), 2)
        self.assertEqual(solution.beadOrnaments([2, 2]), 4)
        self.assertEqual(solution.beadOrnaments([4]), 16)
        self.assertEqual(solution.beadOrnaments([3, 1]), 9)
        self.assertEqual(solution.beadOrnaments([1, 1, 1, 1, 1]), 125)


if __name__ == '__main__':
    unittest.main()
