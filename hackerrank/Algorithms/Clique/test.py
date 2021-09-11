import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.clique(3, 2), 2)
        self.assertEqual(solution.clique(4, 6), 4)
        self.assertEqual(solution.clique(5, 7), 3)

    def test_case_1(self):
        self.assertEqual(solution.clique(5, 7), 3)
        self.assertEqual(solution.clique(7, 21), 7)
        self.assertEqual(solution.clique(15, 144), 16)


if __name__ == '__main__':
    unittest.main()
