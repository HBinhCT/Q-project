import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.stringReduction('cab'), 2)
        self.assertEqual(solution.stringReduction('bcab'), 1)
        self.assertEqual(solution.stringReduction('ccccc'), 5)

    def test_case_1(self):
        self.assertEqual(solution.stringReduction('abcbcba'), 1)
        self.assertEqual(solution.stringReduction('ababbac'), 2)
        self.assertEqual(solution.stringReduction('abababaccc'), 1)


if __name__ == '__main__':
    unittest.main()
