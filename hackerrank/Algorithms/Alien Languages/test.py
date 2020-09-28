import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.alienLanguages(1, 3), 1)
        self.assertEqual(solution.alienLanguages(2, 3), 3)
        self.assertEqual(solution.alienLanguages(3, 2), 6)


if __name__ == '__main__':
    unittest.main()
