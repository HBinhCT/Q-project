import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.quickSort([4, 5, 3, 7, 2]), [3, 2, 4, 5, 7])


if __name__ == '__main__':
    unittest.main()
