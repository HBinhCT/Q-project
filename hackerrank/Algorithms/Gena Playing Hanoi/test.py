import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.tower_of_hanoi([1, 4, 1]), 3)


if __name__ == '__main__':
    unittest.main()
