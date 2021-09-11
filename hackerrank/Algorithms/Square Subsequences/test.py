import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.squareSubsequences('lrbbmqb'), 3)
        self.assertEqual(solution.squareSubsequences('dar'), 0)
        self.assertEqual(solution.squareSubsequences('wkkyhid'), 1)
        self.assertEqual(solution.squareSubsequences('scd'), 0)
        self.assertEqual(solution.squareSubsequences('jmowfrxsjybldbef'), 4)
        self.assertEqual(solution.squareSubsequences('rcbyn'), 0)
        self.assertEqual(solution.squareSubsequences('dyggxxpklorellnmp'), 6)
        self.assertEqual(solution.squareSubsequences('qfwkho'), 0)
        self.assertEqual(solution.squareSubsequences('mcoqhnwnk'), 1)
        self.assertEqual(solution.squareSubsequences('whsqmgbbuqcljjivs'), 4)
        self.assertEqual(solution.squareSubsequences('dkqtbxixmvtrrbljp'), 5)
        self.assertEqual(solution.squareSubsequences('snfwzqfj'), 1)
        self.assertEqual(solution.squareSubsequences('fadrrwsof'), 2)
        self.assertEqual(solution.squareSubsequences('cnuvqhffbs'), 1)
        self.assertEqual(solution.squareSubsequences('xwpqcaceh'), 1)
        self.assertEqual(solution.squareSubsequences('zvfr'), 0)
        self.assertEqual(solution.squareSubsequences('lnozjkpqpxrjx'), 4)
        self.assertEqual(solution.squareSubsequences('tzyxacbhh'), 1)
        self.assertEqual(solution.squareSubsequences('cqcoend'), 1)
        self.assertEqual(solution.squareSubsequences('mfgdwdwfcgpxiqvku'), 6)


if __name__ == '__main__':
    unittest.main()
