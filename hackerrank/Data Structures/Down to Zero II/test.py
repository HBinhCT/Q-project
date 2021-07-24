import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.downToZero(3), 3)
        self.assertEqual(solution.downToZero(4), 3)


if __name__ == '__main__':
    unittest.main()
