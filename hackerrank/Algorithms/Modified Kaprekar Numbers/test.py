import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.kaprekarNumbers(1, 100)
        self.assertEqual(text_trap.getvalue(), '1 9 45 55 99\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.kaprekarNumbers(100, 300)
        self.assertEqual(text_trap.getvalue(), '297\n')


if __name__ == '__main__':
    unittest.main()
