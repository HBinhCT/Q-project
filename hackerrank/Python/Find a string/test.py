import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.count_substring('ABCDCDC', 'CDC'), 2)


if __name__ == '__main__':
    unittest.main()
