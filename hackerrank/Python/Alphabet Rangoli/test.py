import io
import unittest
from contextlib import redirect_stdout
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.print_rangoli(5)
        self.assertEqual(text_trap.getvalue(),
                         '--------e--------\n' +
                         '------e-d-e------\n' +
                         '----e-d-c-d-e----\n' +
                         '--e-d-c-b-c-d-e--\n' +
                         'e-d-c-b-a-b-c-d-e\n' +
                         '--e-d-c-b-c-d-e--\n' +
                         '----e-d-c-d-e----\n' +
                         '------e-d-e------\n' +
                         '--------e--------\n')


if __name__ == '__main__':
    unittest.main()
