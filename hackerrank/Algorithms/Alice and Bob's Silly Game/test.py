import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.sillyGame(1), 'Bob')
        self.assertEqual(solution.sillyGame(2), 'Alice')
        self.assertEqual(solution.sillyGame(5), 'Alice')


if __name__ == '__main__':
    unittest.main()
