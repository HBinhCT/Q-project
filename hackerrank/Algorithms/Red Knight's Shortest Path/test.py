import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.printShortestPath(7, 6, 6, 0, 1)
        self.assertEqual(text_trap.getvalue(), '4\nUL UL UL L\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.printShortestPath(6, 5, 1, 0, 5)
        self.assertEqual(text_trap.getvalue(), 'Impossible\n')

    def test_case_2(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.printShortestPath(7, 0, 3, 4, 3)
        self.assertEqual(text_trap.getvalue(), '2\nLR LL\n')


if __name__ == '__main__':
    unittest.main()
