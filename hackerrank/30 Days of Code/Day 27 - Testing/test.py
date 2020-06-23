import io
import unittest
from contextlib import redirect_stdout


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(), 'OK\n')


if __name__ == '__main__':
    unittest.main()
