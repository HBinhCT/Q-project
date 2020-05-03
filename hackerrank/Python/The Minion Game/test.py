import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.minion_game('BANANA')
        self.assertEqual(text_trap.getvalue(), 'Stuart 12\n')


if __name__ == '__main__':
    unittest.main()
