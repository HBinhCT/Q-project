import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.main([
                ('riya', 'riya@gmail.com'),
                ('julia', 'julia@julia.me'),
                ('julia', 'sjulia@gmail.com'),
                ('julia', 'julia@gmail.com'),
                ('samantha', 'samantha@gmail.com'),
                ('tanya', 'tanya@gmail.com'),
            ])
        self.assertEqual(text_trap.getvalue(),
                         'julia\n'
                         + 'julia\n'
                         + 'riya\n'
                         + 'samantha\n'
                         + 'tanya\n')


if __name__ == '__main__':
    unittest.main()
