import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.minimumPasses(3, 1, 2, 12), 3)

    def test_case_1(self):
        self.assertEqual(solution.minimumPasses(1, 1, 6, 45), 16)

    def test_case_2(self):
        self.assertEqual(solution.minimumPasses(5184889632, 5184889632, 20, 10000), 1)


if __name__ == '__main__':
    unittest.main()
