import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.print_full_name('Ross', 'Taylor')
        self.assertEqual(text_trap.getvalue(), 'Hello Ross Taylor! You just delved into python.\n')


if __name__ == '__main__':
    unittest.main()
