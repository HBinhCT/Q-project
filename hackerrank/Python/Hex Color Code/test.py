import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '11',
        '#BED',
        '{',
        '    color: #FfFdF8; background-color:#aef;',
        '    font-size: 123px;',
        '',
        '}',
        '#Cab',
        '{',
        '    background-color: #ABC;',
        '    border: 2px dashed #fff;',
        '}',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '#FfFdF8\n' +
                         '#aef\n' +
                         '#ABC\n' +
                         '#fff\n')


if __name__ == '__main__':
    unittest.main()
