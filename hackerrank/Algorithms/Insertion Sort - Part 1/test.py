import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.insertionSort1(5, [2, 4, 6, 8, 3])
        self.assertEqual(text_trap.getvalue(), "2 4 6 8 8\n2 4 6 6 8\n2 4 4 6 8\n2 3 4 6 8\n")


if __name__ == '__main__':
    unittest.main()
