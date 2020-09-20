import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.fairCut(2, [4, 3, 1, 2]), 6)

    def test_case_1(self):
        self.assertEqual(solution.fairCut(1, [3, 3, 3, 1]), 2)


if __name__ == '__main__':
    unittest.main()
