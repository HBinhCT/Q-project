import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.misereNim([1, 1]), 'First')
        self.assertEqual(solution.misereNim([2, 1, 3]), 'Second')
        self.assertEqual(solution.misereNim([9, 8, 4, 4, 4, 7]), 'First')


if __name__ == '__main__':
    unittest.main()
