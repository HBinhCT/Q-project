import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.decentNumber(1)
            solution.decentNumber(3)
            solution.decentNumber(5)
            solution.decentNumber(11)
        self.assertEqual(text_trap.getvalue(),
                         '-1\n' +
                         '555\n' +
                         '33333\n' +
                         '55555533333\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.decentNumber(15)
            solution.decentNumber(13)
        self.assertEqual(text_trap.getvalue(),
                         '555555555555555\n' +
                         '5553333333333\n')


if __name__ == '__main__':
    unittest.main()
