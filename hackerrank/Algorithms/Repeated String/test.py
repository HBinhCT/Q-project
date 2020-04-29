import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.repeatedString('aba', 10), 7)

    def test_case_1(self):
        self.assertEqual(solution.repeatedString('a', 1000000000000), 1000000000000)


if __name__ == '__main__':
    unittest.main()
