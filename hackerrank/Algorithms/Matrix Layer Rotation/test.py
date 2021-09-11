import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.matrixRotation(
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16],
                ], 1)
        self.assertEqual(text_trap.getvalue(),
                         '2 3 4 8 \n'
                         + '1 7 11 12 \n'
                         + '5 6 10 16 \n'
                         + '9 13 14 15 \n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.matrixRotation(
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16],
                ], 2)
        self.assertEqual(text_trap.getvalue(),
                         '3 4 8 12 \n'
                         + '2 11 10 16 \n'
                         + '1 7 6 15 \n'
                         + '5 9 13 14 \n')

    def test_case_2(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.matrixRotation(
                [
                    [1, 2, 3, 4],
                    [7, 8, 9, 10],
                    [13, 14, 15, 16],
                    [19, 20, 21, 22],
                    [25, 26, 27, 28],
                ], 7)
        self.assertEqual(text_trap.getvalue(),
                         '28 27 26 25 \n'
                         + '22 9 15 19 \n'
                         + '16 8 21 13 \n'
                         + '10 14 20 7 \n'
                         + '4 3 2 1 \n')

    def test_case_3(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.matrixRotation(
                [
                    [1, 1],
                    [1, 1],
                ], 3)
        self.assertEqual(text_trap.getvalue(),
                         '1 1 \n'
                         + '1 1 \n')


if __name__ == '__main__':
    unittest.main()
