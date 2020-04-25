import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.steadyGene('GAAATAAA'), 5)

    def test_case_1(self):
        self.assertEqual(my_code.steadyGene('TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC'), 5)


if __name__ == '__main__':
    unittest.main()
