import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.pokerNim(5, [1, 2]), 'First')
        self.assertEqual(solution.pokerNim(5, [2, 1, 3]), 'Second')


if __name__ == '__main__':
    unittest.main()
