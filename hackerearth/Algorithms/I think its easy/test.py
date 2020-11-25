import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        'ab cd e j asd ljffg df',
        'a a b b c c',
        'xy yx zxy zx xzy xxx',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'e j ab cd df asd ljffg\n' +
                         'a a b b c c\n' +
                         'xy yx zx zxy xzy xxx\n')


if __name__ == '__main__':
    unittest.main()
