import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.counterGame(6), 'Richard')


if __name__ == '__main__':
    unittest.main()
