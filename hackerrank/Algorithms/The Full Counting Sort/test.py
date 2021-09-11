import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.countSort(
                [
                    [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [4, 'ij'], [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'],
                    [0, 'ij'], [4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'],
                    [4, 'is'], [2, 'to'], [4, 'the']
                ]
            )
        self.assertEqual(text_trap.getvalue(), "- - - - - to be or not to be - that is the question - - - -\n")

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.countSort(
                [[1, 'e'], [2, 'a'], [1, 'b'], [3, 'a'], [4, 'f'], [1, 'f'], [2, 'a'], [1, 'e'], [1, 'b'], [1, 'c']]
            )
        self.assertEqual(text_trap.getvalue(), "- - f e b c - a - -\n")


if __name__ == '__main__':
    unittest.main()
