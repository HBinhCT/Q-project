import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.alternatingCharacters('AAAA'), 3)
        self.assertEqual(solution.alternatingCharacters('BBBBB'), 4)
        self.assertEqual(solution.alternatingCharacters('ABABABAB'), 0)
        self.assertEqual(solution.alternatingCharacters('BABABA'), 0)
        self.assertEqual(solution.alternatingCharacters('AAABBB'), 4)

    def test_case_1(self):
        self.assertEqual(solution.alternatingCharacters('AAABBBAABB'), 6)
        self.assertEqual(solution.alternatingCharacters('AABBAABB'), 4)
        self.assertEqual(solution.alternatingCharacters('ABABABAA'), 1)

    def test_case_2(self):
        self.assertEqual(solution.alternatingCharacters('ABBABBAA'), 3)


if __name__ == '__main__':
    unittest.main()
