import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.insertionSort2(6, [1, 4, 3, 5, 6, 2])
        self.assertEqual(text_trap.getvalue(), "1 4 3 5 6 2\n1 3 4 5 6 2\n1 3 4 5 6 2\n1 3 4 5 6 2\n1 2 3 4 5 6\n")

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.insertionSort2(8, [8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(
            text_trap.getvalue(),
            "7 8 6 5 4 3 2 1\n6 7 8 5 4 3 2 1\n5 6 7 8 4 3 2 1\n4 5 6 7 8 3 2 1\n3 4 5 6 7 8 2 1\n2 3 4 5 6 7 8 1\n1 2 3 4 5 6 7 8\n"
        )


if __name__ == '__main__':
    unittest.main()
