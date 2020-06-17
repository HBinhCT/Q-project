import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.main([1, 4, 3, 2])
        self.assertEqual(text_trap.getvalue(), '2 3 4 1\n')


if __name__ == '__main__':
    unittest.main()
