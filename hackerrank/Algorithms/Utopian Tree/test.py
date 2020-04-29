import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.utopianTree(0), 1)
        self.assertEqual(solution.utopianTree(1), 2)

    def test_case_1(self):
        self.assertEqual(solution.utopianTree(4), 7)
        self.assertEqual(solution.utopianTree(3), 6)


if __name__ == '__main__':
    unittest.main()
