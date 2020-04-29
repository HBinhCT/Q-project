import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.simpleArraySum([1, 2, 3, 4, 10, 11]), 31)


if __name__ == '__main__':
    unittest.main()
