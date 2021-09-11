import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.stoneDivision(15, [5, 2, 3]), 'Second')


if __name__ == '__main__':
    unittest.main()
