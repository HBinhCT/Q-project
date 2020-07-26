import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.rustMurderer(4, [[1, 2], [2, 3], [1, 4]], 1), [3, 1, 2])
        self.assertEqual(solution.rustMurderer(4, [[1, 2], [2, 3]], 2), [2, 2, 1])


if __name__ == '__main__':
    unittest.main()
