import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.countArray(4, 3, 2), 3)


if __name__ == '__main__':
    unittest.main()
