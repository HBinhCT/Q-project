import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.gamingArray([5, 2, 6, 3, 4]), 'ANDY')
        self.assertEqual(solution.gamingArray([3, 1]), 'BOB')

    def test_case_1(self):
        self.assertEqual(solution.gamingArray([1, 3, 5, 7, 9]), 'BOB')
        self.assertEqual(solution.gamingArray([7, 4, 6, 5, 9]), 'ANDY')


if __name__ == '__main__':
    unittest.main()
