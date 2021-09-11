import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.legoBlocks(2, 2), 3)
        self.assertEqual(solution.legoBlocks(3, 2), 7)
        self.assertEqual(solution.legoBlocks(2, 3), 9)
        self.assertEqual(solution.legoBlocks(4, 4), 3375)

    def test_case_1(self):
        self.assertEqual(solution.legoBlocks(4, 5), 35714)
        self.assertEqual(solution.legoBlocks(4, 6), 447902)
        self.assertEqual(solution.legoBlocks(4, 7), 5562914)
        self.assertEqual(solution.legoBlocks(5, 4), 29791)
        self.assertEqual(solution.legoBlocks(6, 4), 250047)
        self.assertEqual(solution.legoBlocks(7, 4), 2048383)


if __name__ == '__main__':
    unittest.main()
