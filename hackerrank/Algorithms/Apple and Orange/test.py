import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6])
        self.assertEqual(text_trap.getvalue(), "1\n1\n")


if __name__ == '__main__':
    unittest.main()
