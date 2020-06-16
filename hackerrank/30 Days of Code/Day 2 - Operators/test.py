import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.solve(12.00, 20, 8)
        self.assertEqual(text_trap.getvalue(), '15\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.solve(15.50, 15, 10)
        self.assertEqual(text_trap.getvalue(), '19\n')


if __name__ == '__main__':
    unittest.main()
