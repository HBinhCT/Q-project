import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.componentsInGraph([
            [1, 6],
            [2, 7],
            [3, 8],
            [4, 9],
            [2, 6],
        ]), (2, 4))


if __name__ == '__main__':
    unittest.main()
