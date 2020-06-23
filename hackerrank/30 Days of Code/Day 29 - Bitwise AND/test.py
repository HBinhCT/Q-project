import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.main(5, 2)
            solution.main(8, 5)
            solution.main(2, 2)
        self.assertEqual(text_trap.getvalue(),
                         '1\n'
                         + '4\n'
                         + '0\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.main(9, 2)
            solution.main(8, 3)
        self.assertEqual(text_trap.getvalue(),
                         '1\n'
                         + '2\n')


if __name__ == '__main__':
    unittest.main()
