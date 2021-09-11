import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.stonePiles([4]), 'BOB')
        self.assertEqual(solution.stonePiles([1, 2]), 'BOB')
        self.assertEqual(solution.stonePiles([1, 3, 4]), 'ALICE')
        self.assertEqual(solution.stonePiles([8]), 'BOB')


if __name__ == '__main__':
    unittest.main()
