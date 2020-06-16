import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.main(2)
        self.assertEqual(text_trap.getvalue(),
                         '2 x 1 = 2' + '\n' +
                         '2 x 2 = 4' + '\n' +
                         '2 x 3 = 6' + '\n' +
                         '2 x 4 = 8' + '\n' +
                         '2 x 5 = 10' + '\n' +
                         '2 x 6 = 12' + '\n' +
                         '2 x 7 = 14' + '\n' +
                         '2 x 8 = 16' + '\n' +
                         '2 x 9 = 18' + '\n' +
                         '2 x 10 = 20' + '\n')


if __name__ == '__main__':
    unittest.main()
