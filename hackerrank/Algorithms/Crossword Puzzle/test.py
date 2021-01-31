import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(
            solution.crosswordPuzzle(
                [
                    '+-++++++++',
                    '+-++++++++',
                    '+-++++++++',
                    '+-----++++',
                    '+-+++-++++',
                    '+-+++-++++',
                    '+++++-++++',
                    '++------++',
                    '+++++-++++',
                    '+++++-++++',
                ],
                'LONDON;DELHI;ICELAND;ANKARA',
            ),
            [
                '+L++++++++',
                '+O++++++++',
                '+N++++++++',
                '+DELHI++++',
                '+O+++C++++',
                '+N+++E++++',
                '+++++L++++',
                '++ANKARA++',
                '+++++N++++',
                '+++++D++++',
            ]
        )

    def test_case_1(self):
        self.assertEqual(
            solution.crosswordPuzzle(
                [
                    '+-++++++++',
                    '+-++++++++',
                    '+-------++',
                    '+-++++++++',
                    '+-++++++++',
                    '+------+++',
                    '+-+++-++++',
                    '+++++-++++',
                    '+++++-++++',
                    '++++++++++',
                ],
                'AGRA;NORWAY;ENGLAND;GWALIOR',
            ),
            [
                '+E++++++++',
                '+N++++++++',
                '+GWALIOR++',
                '+L++++++++',
                '+A++++++++',
                '+NORWAY+++',
                '+D+++G++++',
                '+++++R++++',
                '+++++A++++',
                '++++++++++',
            ]
        )

    def test_case_2(self):
        self.assertEqual(
            solution.crosswordPuzzle(
                [
                    'XXXXXX-XXX',
                    'XX------XX',
                    'XXXXXX-XXX',
                    'XXXXXX-XXX',
                    'XXX------X',
                    'XXXXXX-X-X',
                    'XXXXXX-X-X',
                    'XXXXXXXX-X',
                    'XXXXXXXX-X',
                    'XXXXXXXX-X',
                ],
                'ICELAND;MEXICO;PANAMA;ALMATY',
            ),
            [
                'XXXXXXIXXX',
                'XXMEXICOXX',
                'XXXXXXEXXX',
                'XXXXXXLXXX',
                'XXXPANAMAX',
                'XXXXXXNXLX',
                'XXXXXXDXMX',
                'XXXXXXXXAX',
                'XXXXXXXXTX',
                'XXXXXXXXYX',
            ]
        )


if __name__ == '__main__':
    unittest.main()
