import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.pairs(2, [1, 5, 3, 4, 2]), 3)

    def test_case_1(self):
        self.assertEqual(
            solution.pairs(1, [363374326, 364147530, 61825163, 1073065718, 1281246024, 1399469912, 428047635, 491595254,
                               879792181, 1069262793]), 0)

    def test_case_2(self):
        self.assertEqual(solution.pairs(2, [1, 3, 5, 8, 6, 4, 2]), 5)


if __name__ == '__main__':
    unittest.main()
