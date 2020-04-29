import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.extraLongFactorials(25)
        self.assertEqual(text_trap.getvalue(), "15511210043330985984000000\n")

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.extraLongFactorials(45)
        self.assertEqual(text_trap.getvalue(), "119622220865480194561963161495657715064383733760000000000\n")


if __name__ == '__main__':
    unittest.main()
