import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.main(
                {
                    'Krishna': [67, 68, 69],
                    'Arjun': [70, 98, 63],
                    'Malika': [52, 56, 60],
                },
                'Malika')
        self.assertEqual(text_trap.getvalue(), '56.00\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.main(
                {
                    'Harsh': [25, 26.5, 28],
                    'Anurag': [26, 28, 30],
                },
                'Harsh')
        self.assertEqual(text_trap.getvalue(), '26.50\n')


if __name__ == '__main__':
    unittest.main()
