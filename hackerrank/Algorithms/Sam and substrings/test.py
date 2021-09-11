import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.substrings('16'), 23)

    def test_case_1(self):
        self.assertEqual(solution.substrings('123'), 164)


if __name__ == '__main__':
    unittest.main()
