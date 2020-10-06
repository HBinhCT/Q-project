import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.redJohn(1), 0)
        self.assertEqual(solution.redJohn(7), 3)

    def test_case_1(self):
        self.assertEqual(solution.redJohn(3), 0)
        self.assertEqual(solution.redJohn(5), 2)
        self.assertEqual(solution.redJohn(8), 4)


if __name__ == '__main__':
    unittest.main()
