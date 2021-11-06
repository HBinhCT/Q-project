import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readlines', return_value=[
        'int t; //variable t',
        't->a=0;  //t->a does something',
        'return 0;',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         'int t; //variable t\n' +
                         't.a=0;  //t->a does something\n' +
                         'return 0;\n')


if __name__ == '__main__':
    unittest.main()
