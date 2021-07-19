import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.equalStacks(
            [3, 2, 1, 1, 1],
            [4, 3, 2],
            [1, 1, 4, 1],
        ), 5)


if __name__ == '__main__':
    unittest.main()
