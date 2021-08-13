import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.noPrefix([
                'aab',
                'defgab',
                'abcde',
                'aabcde',
                'cedaaa',
                'bbbbbbbbbb',
                'jabjjjad',
            ])
        self.assertEqual(text_trap.getvalue(),
                         'BAD SET\n' +
                         'aabcde\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.noPrefix([
                'aab',
                'aac',
                'aacghgh',
                'aabghgh',
            ])
        self.assertEqual(text_trap.getvalue(),
                         'BAD SET\n' +
                         'aacghgh\n')


if __name__ == '__main__':
    unittest.main()
