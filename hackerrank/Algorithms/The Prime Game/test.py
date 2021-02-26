import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.winner([10, 10]), 'Sandy')
        self.assertEqual(solution.winner([2, 2, 3]), 'Manasa')


if __name__ == '__main__':
    unittest.main()
