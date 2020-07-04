import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.countLuck(
            [
                '*.M',
                '.X.',
            ], 1), 'Impressed')
        self.assertEqual(solution.countLuck(
            [
                '.X.X......X',
                '.X*.X.XXX.X',
                '.XX.X.XM...',
                '......XXXX.',
            ], 3), 'Impressed')
        self.assertEqual(solution.countLuck(
            [
                '.X.X......X',
                '.X*.X.XXX.X',
                '.XX.X.XM...',
                '......XXXX.',
            ], 4), 'Oops!')

    def test_case_1(self):
        self.assertEqual(solution.countLuck(
            [
                '*.X',
                'X.X',
                'X.M',
            ], 0), 'Impressed')
        self.assertEqual(solution.countLuck(
            [
                '*.X',
                'X.X',
                '..M',
            ], 1), 'Impressed')
        self.assertEqual(solution.countLuck(
            [
                '*..',
                'X.X',
                '..M',
            ], 1), 'Oops!')


if __name__ == '__main__':
    unittest.main()
