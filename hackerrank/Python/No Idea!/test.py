import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.happiness([1, 5, 3], {1, 3}, {5, 7}), 1)


if __name__ == '__main__':
    unittest.main()
