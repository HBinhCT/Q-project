import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.aOrB(8, '2B', '9F', '58')
        self.assertEqual(text_trap.getvalue(),
                         '8\n' +
                         '58\n')

        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.aOrB(5, 'B9', '40', '5A')
        self.assertEqual(text_trap.getvalue(),
                         '18\n' +
                         '42\n')

        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.aOrB(2, '91', 'BE', 'A8')
        self.assertEqual(text_trap.getvalue(), '-1\n')


if __name__ == '__main__':
    unittest.main()
