import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.getCost(5, [1, 3, 1, 4, 2], [2, 5, 4, 5, 3], [60, 70, 120, 150, 80])
        self.assertEqual(text_trap.getvalue(), '80\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.getCost(5, [1, 2, 3, 4, 1, 3], [2, 3, 4, 5, 3, 5], [30, 50, 70, 90, 70, 85])
        self.assertEqual(text_trap.getvalue(), '85\n')


if __name__ == '__main__':
    unittest.main()
