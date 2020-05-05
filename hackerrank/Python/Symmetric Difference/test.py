import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.symmetric_difference({2, 4, 5, 9}, {2, 4, 11, 12})
        self.assertEqual(text_trap.getvalue(), '5\n9\n11\n12\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.symmetric_difference({8, -10}, {5, 6, 7})
        self.assertEqual(text_trap.getvalue(), '-10\n5\n6\n7\n8\n')


if __name__ == '__main__':
    unittest.main()
