import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.bomberMan(
            3, [
                '.......',
                '...O...',
                '....O..',
                '.......',
                'OO.....',
                'OO.....',
            ]),
            [
                'OOO.OOO',
                'OO...OO',
                'OOO...O',
                '..OO.OO',
                '...OOOO',
                '...OOOO',
            ])

    def test_case_1(self):
        self.assertEqual(solution.bomberMan(
            5, [
                '.......',
                '...O.O.',
                '....O..',
                '..O....',
                'OO...OO',
                'OO.O...',
            ]),
            [
                '.......',
                '...O.O.',
                '...OO..',
                '..OOOO.',
                'OOOOOOO',
                'OOOOOOO',
            ])


if __name__ == '__main__':
    unittest.main()
