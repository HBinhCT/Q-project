import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.almostSorted([4, 2])
        self.assertEqual(text_trap.getvalue(), "yes\nswap 1 2\n")

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.almostSorted([3, 1, 2])
        self.assertEqual(text_trap.getvalue(), "no\n")

    def test_case_2(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.almostSorted([1, 5, 4, 3, 2, 6])
        self.assertEqual(text_trap.getvalue(), "yes\nreverse 2 5\n")


if __name__ == '__main__':
    unittest.main()
