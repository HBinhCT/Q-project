import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.whatsNext([4, 1, 3, 2, 4])
        self.assertEqual(text_trap.getvalue(),
                         '7\n' +
                         '4 1 3 1 1 1 3\n')


if __name__ == '__main__':
    unittest.main()
