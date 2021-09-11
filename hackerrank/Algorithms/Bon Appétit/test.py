import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.bonAppetit([3, 10, 2, 9], 1, 12)
        self.assertEqual(text_trap.getvalue(), "5\n")

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.bonAppetit([3, 10, 2, 9], 1, 7)
        self.assertEqual(text_trap.getvalue(), "Bon Appetit\n")


if __name__ == '__main__':
    unittest.main()
