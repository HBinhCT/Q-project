import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.split_and_join('this is a string'), 'this-is-a-string')


if __name__ == '__main__':
    unittest.main()
