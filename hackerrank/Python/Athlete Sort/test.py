import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.main([[10, 2, 5],
                           [7, 1, 0],
                           [9, 9, 9],
                           [1, 23, 12],
                           [6, 5, 9]],
                          1)
        self.assertEqual(text_trap.getvalue(),
                         '7 1 0' + '\n' +
                         '10 2 5' + '\n' +
                         '6 5 9' + '\n' +
                         '9 9 9' + '\n' +
                         '1 23 12' + '\n')


if __name__ == '__main__':
    unittest.main()
