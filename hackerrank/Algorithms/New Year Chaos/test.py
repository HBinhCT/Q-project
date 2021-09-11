import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.minimumBribes([2, 1, 5, 3, 4])
        self.assertEqual(text_trap.getvalue(), '3\n')

        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.minimumBribes([2, 5, 1, 3, 4])
        self.assertEqual(text_trap.getvalue(), 'Too chaotic\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.minimumBribes([5, 1, 2, 3, 7, 8, 6, 4])
        self.assertEqual(text_trap.getvalue(), 'Too chaotic\n')

        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])
        self.assertEqual(text_trap.getvalue(), '7\n')

    def test_case_2(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.minimumBribes([1, 2, 5, 3, 4, 7, 8, 6])
        self.assertEqual(text_trap.getvalue(), '4\n')


if __name__ == '__main__':
    unittest.main()
