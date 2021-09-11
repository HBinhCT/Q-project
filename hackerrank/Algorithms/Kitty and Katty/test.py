import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.winner(2), 'Kitty')
        self.assertEqual(solution.winner(3), 'Katty')


if __name__ == '__main__':
    unittest.main()
