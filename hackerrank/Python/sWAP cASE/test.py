import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.swap_case('HackerRank.com presents "Pythonist 2".'),
                         'hACKERrANK.COM PRESENTS "pYTHONIST 2".')


if __name__ == '__main__':
    unittest.main()
