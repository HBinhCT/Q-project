import io
import unittest
from contextlib import redirect_stdout
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            my_code.miniMaxSum([1, 2, 3, 4, 5])
        self.assertEqual(text_trap.getvalue(), "10 14\n")

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            my_code.miniMaxSum([7, 69, 2, 221, 8974])
        self.assertEqual(text_trap.getvalue(), "299 9271\n")


if __name__ == '__main__':
    unittest.main()
