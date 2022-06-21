import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2',
        '6 3',
        'arjit',
        'tijra',
        'genius',
        'chanda',
        'ashish',
        'arjit',
        '4 2',
        'bond',
        'coder',
        'bond',
        'lol',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'Possible\n' +
                         'Not possible\n')


if __name__ == '__main__':
    unittest.main()
