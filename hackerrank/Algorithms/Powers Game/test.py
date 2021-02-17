import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.powersGame(2), 'First')


if __name__ == '__main__':
    unittest.main()
