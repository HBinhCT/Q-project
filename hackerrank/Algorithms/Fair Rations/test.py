import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.fairRations([2, 3, 4, 5, 6]), 4)

    def test_case_1(self):
        self.assertEqual(solution.fairRations([1, 2]), 'NO')


if __name__ == '__main__':
    unittest.main()
