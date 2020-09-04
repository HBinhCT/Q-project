import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.pylons(2, [0, 1, 1, 1, 1, 0]), 2)

    def test_case_1(self):
        self.assertEqual(solution.pylons(2, [0, 1, 0, 0, 0, 1, 0]), -1)

    def test_case_2(self):
        self.assertEqual(solution.pylons(3, [0, 1, 0, 0, 0, 1, 1, 1, 1, 1]), 3)


if __name__ == '__main__':
    unittest.main()
