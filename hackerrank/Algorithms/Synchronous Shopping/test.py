import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(
            solution.shop(
                5,
                5,
                ['1 1',
                 '1 2',
                 '1 3',
                 '1 4',
                 '1 5'],
                [[1, 2, 10],
                 [1, 3, 10],
                 [2, 4, 10],
                 [3, 5, 10],
                 [4, 5, 10]]
            ),
            30)

    def test_case_1(self):
        self.assertEqual(
            solution.shop(
                6,
                3,
                ['2 1 2',
                 '1 3',
                 '0',
                 '2 1 3',
                 '1 2',
                 '1 3'],
                [[1, 2, 572],
                 [4, 2, 913],
                 [2, 6, 220],
                 [1, 3, 579],
                 [2, 3, 808],
                 [5, 3, 298],
                 [6, 1, 927],
                 [4, 5, 171],
                 [1, 5, 671],
                 [2, 5, 463]]
            ),
            792)


if __name__ == '__main__':
    unittest.main()
