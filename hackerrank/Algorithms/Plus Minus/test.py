import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.plusMinus([-4, 3, -9, 0, 4, 1])
        self.assertEqual(text_trap.getvalue(), "0.500000\n0.333333\n0.166667\n")

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.plusMinus([1, 2, 3, -1, -2, -3, 0, 0])
        self.assertEqual(text_trap.getvalue(), "0.375000\n0.375000\n0.250000\n")


if __name__ == '__main__':
    unittest.main()
