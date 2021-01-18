import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.xorSequence(2, 4), 7)
        self.assertEqual(solution.xorSequence(2, 8), 9)
        self.assertEqual(solution.xorSequence(5, 9), 15)

    def test_case_1(self):
        self.assertEqual(solution.xorSequence(3, 5), 5)
        self.assertEqual(solution.xorSequence(4, 6), 2)
        self.assertEqual(solution.xorSequence(15, 20), 22)


if __name__ == '__main__':
    unittest.main()
