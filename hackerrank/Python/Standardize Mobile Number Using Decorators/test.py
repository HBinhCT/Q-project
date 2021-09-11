import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.sort_phone(['07895462130', '919875641230', '9195969878'])
        self.assertEqual(text_trap.getvalue(), '+91 78954 62130\n+91 91959 69878\n+91 98756 41230\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.sort_phone(['09191919191', '9100256236', '+919593621456'])
        self.assertEqual(text_trap.getvalue(), '+91 91002 56236\n+91 91919 19191\n+91 95936 21456\n')


if __name__ == '__main__':
    unittest.main()
