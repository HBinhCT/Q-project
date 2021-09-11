import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.steadyGene('GAAATAAA'), 5)

    def test_case_1(self):
        self.assertEqual(solution.steadyGene('TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC'), 5)


if __name__ == '__main__':
    unittest.main()
